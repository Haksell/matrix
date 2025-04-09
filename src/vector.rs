use {crate::field::Field, core::ops::Index};

#[derive(Clone, Debug, PartialEq)]
pub struct Vector<K: Field, const N: usize> {
    values: [K; N],
}

#[macro_export]
macro_rules! v {
    ($($x:expr),+ $(,)?) => {{
        $crate::Vector::from([$($x),*])
    }};
}

impl<K: Field, const N: usize> Vector<K, N> {
    pub const fn from(values: [K; N]) -> Self {
        Self { values }
    }

    pub fn zeros() -> Self {
        Self {
            values: [K::zero(); N],
        }
    }

    pub fn ones() -> Self {
        Self {
            values: [K::one(); N],
        }
    }

    pub fn full(value: K) -> Self {
        Self { values: [value; N] }
    }

    pub const fn len(&self) -> usize {
        N
    }
}

impl<K: Field, const N: usize> Index<usize> for Vector<K, N> {
    type Output = K;

    fn index(&self, i: usize) -> &Self::Output {
        &self.values[i]
    }
}

macro_rules! impl_vector_vector {
    ($lhs:ty, $rhs:ty) => {
        impl<K: Field, const N: usize> core::ops::Add<$rhs> for $lhs {
            type Output = Vector<K, N>;

            fn add(self, rhs: $rhs) -> Vector<K, N> {
                Vector {
                    values: core::array::from_fn(|i| self.values[i] + rhs.values[i]),
                }
            }
        }

        impl<K: Field, const N: usize> core::ops::Sub<$rhs> for $lhs {
            type Output = Vector<K, N>;

            fn sub(self, rhs: $rhs) -> Vector<K, N> {
                Vector {
                    values: core::array::from_fn(|i| self.values[i] - rhs.values[i]),
                }
            }
        }
    };
}

impl_vector_vector!(Vector<K, N>, Vector<K, N>);
impl_vector_vector!(Vector<K, N>, &Vector<K, N>);
impl_vector_vector!(&Vector<K, N>, Vector<K, N>);
impl_vector_vector!(&Vector<K, N>, &Vector<K, N>);

macro_rules! impl_vector_scalar {
    ($lhs:ty, $rhs:ty) => {
        impl<K: Field, const N: usize> core::ops::Mul<$rhs> for $lhs {
            type Output = Vector<K, N>;

            fn mul(self, rhs: $rhs) -> Self::Output {
                Vector {
                    values: core::array::from_fn(|i| self.values[i] * rhs),
                }
            }
        }
    };
}

impl_vector_scalar!(Vector<K, N>, K);
impl_vector_scalar!(&Vector<K, N>, K);
impl_vector_scalar!(Vector<K, N>, &K);
impl_vector_scalar!(&Vector<K, N>, &K);

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_constructors() {
        assert_eq!(Vector::from([1., 2., 3.14, 4.2]), v![1., 2., 3.14, 4.2]);
        assert_eq!(Vector::<f32, 3>::zeros().values, [0., 0., 0.]);
        assert_eq!(Vector::<f32, 3>::ones(), Vector::full(1.));
    }

    #[test]
    fn test_len() {
        assert_eq!(v![1., 2., 3., 4.].len(), 4);
    }

    #[test]
    fn test_index() {
        let v = v![1., 2., 3.];
        assert_eq!(v[0], 1.);
        assert_eq!(v[1], 2.);
        assert_eq!(v[2], 3.);
    }

    #[test]
    #[should_panic]
    fn test_index_invalid() {
        let v = v![1., 2., 3.];
        v[3];
    }

    #[test]
    fn test_add() {
        assert_eq!(
            Vector::<f32, 42>::zeros() + Vector::<f32, 42>::zeros(),
            Vector::<f32, 42>::zeros()
        );
        assert_eq!(v![1., 2.] + &v![3., 4.], v![4., 6.]);
        assert_eq!(&v![1., 2.] + v![3., 4.], v![4., 6.]);
        assert_eq!(&v![1., 2.5, 0.] + &v![3., -4., 0.], v![4., -1.5, 0.]);
    }

    #[test]
    fn test_sub() {
        assert_eq!(
            Vector::<f32, 42>::zeros() - Vector::<f32, 42>::zeros(),
            Vector::<f32, 42>::zeros()
        );
        assert_eq!(v![1., 2.] - &v![3., 4.], v![-2., -2.]);
        assert_eq!(&v![1., 2.] - v![3., 4.], v![-2., -2.]);
        assert_eq!(&v![1., 2.5, 0.] - &v![3., -4., 0.], v![-2., 6.5, 0.]);
    }

    #[test]
    fn test_scalar_mul() {
        assert_eq!(Vector::<f32, 42>::zeros() * 7., Vector::zeros());
        assert_eq!(v![1., 2.] * &3., v![3., 6.]);
        assert_eq!(&v![1., 2.] * -2.5, v![-2.5, -5.]);
        assert_eq!(&v![1., 2.5, 0.] * &0., v![0., 0., 0.]);
    }
}
