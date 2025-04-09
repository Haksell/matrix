use crate::field::Field;

#[derive(Clone, Debug, PartialEq)]
pub struct Vector<K: Field, const N: usize> {
    values: [K; N],
}

impl<K: Field, const N: usize> Vector<K, N> {
    pub const fn from(values: [K; N]) -> Self {
        Self { values }
    }

    pub const fn len(&self) -> usize {
        N
    }
}

impl<K: Field, const N: usize> Default for Vector<K, N> {
    fn default() -> Self {
        Self {
            values: [K::default(); N],
        }
    }
}

macro_rules! impl_add_for_vector {
    ($lhs:ty, $rhs:ty) => {
        impl<K: Field, const N: usize> core::ops::Add<$rhs> for $lhs {
            type Output = Vector<K, N>;

            fn add(self, rhs: $rhs) -> Vector<K, N> {
                Vector {
                    values: core::array::from_fn(|i| self.values[i] + rhs.values[i]),
                }
            }
        }
    };
}

impl_add_for_vector!(Vector<K, N>, Vector<K, N>);
impl_add_for_vector!(Vector<K, N>, &Vector<K, N>);
impl_add_for_vector!(&Vector<K, N>, Vector<K, N>);
impl_add_for_vector!(&Vector<K, N>, &Vector<K, N>);

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_default() {
        assert_eq!(Vector::<f32, 3>::default().values, [0., 0., 0.]);
    }

    #[test]
    fn test_from() {
        assert_eq!(
            Vector::from([1., 2., 3.14, 4.2]).values,
            [1., 2., 3.14, 4.2]
        );
    }

    #[test]
    fn test_len() {
        assert_eq!(Vector::from([1., 2., 3., 4.]).len(), 4);
    }

    // TODO: more tests
    #[test]
    fn test_add() {
        assert_eq!(
            Vector::<f32, 42>::default() + Vector::<f32, 42>::default(),
            Vector::<f32, 42>::default()
        );
        assert_eq!(
            Vector::from([1., 2.]) + &Vector::from([3., 4.]),
            Vector::from([4., 6.])
        );
        assert_eq!(
            &Vector::from([1., 2.]) + Vector::from([3., 4.]),
            Vector::from([4., 6.])
        );
        assert_eq!(
            &Vector::from([1., 2.5, 0.]) + &Vector::from([3., -4., 0.]),
            Vector::from([4., -1.5, 0.])
        );
    }
}
