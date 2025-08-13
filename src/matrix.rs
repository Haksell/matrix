use {crate::field::Field, core::ops::Index};

#[derive(Clone, Debug, PartialEq)]
pub struct Matrix<K: Field, const H: usize, const W: usize> {
    values: [[K; W]; H],
}

#[macro_export]
macro_rules! m {
    ($($x:expr),+ $(,)?) => {{
        $crate::Matrix::from([$($x),*])
    }};
}

impl<K: Field, const H: usize, const W: usize> Matrix<K, H, W> {
    pub const fn from(values: [[K; W]; H]) -> Self {
        Self { values }
    }

    pub fn zeros() -> Self {
        Self {
            values: [[K::zero(); W]; H],
        }
    }

    pub fn ones() -> Self {
        Self {
            values: [[K::one(); W]; H],
        }
    }

    pub fn full(value: K) -> Self {
        Self {
            values: [[value; W]; H],
        }
    }

    pub const fn height(&self) -> usize {
        H
    }

    pub const fn width(&self) -> usize {
        W
    }

    pub const fn shape(&self) -> (usize, usize) {
        (H, W)
    }

    pub const fn is_square(&self) -> bool {
        H == W
    }
}

impl<K: Field, const H: usize, const W: usize> Index<(usize, usize)> for Matrix<K, H, W> {
    type Output = K;

    fn index(&self, (y, x): (usize, usize)) -> &Self::Output {
        &self.values[y][x]
    }
}

macro_rules! impl_matrix_matrix {
    ($lhs:ty, $rhs:ty) => {
        impl<K: Field, const H: usize, const W: usize> core::ops::Add<$rhs> for $lhs {
            type Output = Matrix<K, H, W>;

            fn add(self, rhs: $rhs) -> Matrix<K, H, W> {
                Matrix {
                    values: core::array::from_fn(|y| {
                        core::array::from_fn(|x| self.values[y][x] + rhs.values[y][x])
                    }),
                }
            }
        }

        impl<K: Field, const H: usize, const W: usize> core::ops::Sub<$rhs> for $lhs {
            type Output = Matrix<K, H, W>;

            fn sub(self, rhs: $rhs) -> Matrix<K, H, W> {
                Matrix {
                    values: core::array::from_fn(|y| {
                        core::array::from_fn(|x| self.values[y][x] - rhs.values[y][x])
                    }),
                }
            }
        }
    };
}

impl_matrix_matrix!(Matrix<K, H, W>, Matrix<K, H, W>);
impl_matrix_matrix!(Matrix<K, H, W>, &Matrix<K, H, W>);
impl_matrix_matrix!(&Matrix<K, H, W>, Matrix<K, H, W>);
impl_matrix_matrix!(&Matrix<K, H, W>, &Matrix<K, H, W>);

macro_rules! impl_matrix_scalar {
    ($matrix:ty, $field:ty) => {
        impl<K: Field, const H: usize, const W: usize> core::ops::Mul<$field> for $matrix {
            type Output = Matrix<K, H, W>;

            fn mul(self, scalar: $field) -> Self::Output {
                Matrix {
                    values: core::array::from_fn(|y| {
                        core::array::from_fn(|x| self.values[y][x] * scalar)
                    }),
                }
            }
        }
    };
}

impl_matrix_scalar!(Matrix<K, H, W>, K);
impl_matrix_scalar!(Matrix<K, H, W>, &K);
impl_matrix_scalar!(&Matrix<K, H, W>, K);
impl_matrix_scalar!(&Matrix<K, H, W>, &K);

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_constructors() {
        assert_eq!(
            Matrix::from([[1., 2.], [3.14, 4.2]]),
            m![[1., 2.], [3.14, 4.2]]
        );
        assert_eq!(
            Matrix::<f32, 3, 2>::zeros().values,
            [[0., 0.], [0., 0.], [0., 0.]]
        );
        assert_eq!(Matrix::<f32, 2, 3>::ones(), Matrix::full(1.));
    }

    #[test]
    fn test_index() {
        let m = m![[0.25, 0.5, 1.], [2., 4., 8.]];
        assert_eq!(m[(0, 0)], 0.25);
        assert_eq!(m[(0, 1)], 0.5);
        assert_eq!(m[(0, 2)], 1.);
        assert_eq!(m[(1, 0)], 2.);
        assert_eq!(m[(1, 1)], 4.);
        assert_eq!(m[(1, 2)], 8.);
    }

    #[test]
    #[should_panic]
    fn test_index_invalid_row() {
        let m = m![[0.25, 0.5, 1.], [2., 4., 8.]];
        m[(2, 0)];
    }

    #[test]
    #[should_panic]
    fn test_index_invalid_col() {
        let m = m![[0.25, 0.5, 1.], [2., 4., 8.]];
        m[(0, 4)];
    }

    #[test]
    fn test_shape() {
        let m = Matrix::<f32, 2, 3>::zeros();
        assert_eq!(m.height(), 2);
        assert_eq!(m.width(), 3);
        assert_eq!(m.shape(), (2, 3));
    }

    #[test]
    fn test_is_square() {
        assert!(!Matrix::<f32, 2, 3>::zeros().is_square());
        assert!(Matrix::<f32, 6, 6>::zeros().is_square());
    }

    #[test]
    fn test_add() {
        assert_eq!(
            Matrix::<f32, 4, 2>::zeros() + Matrix::<f32, 4, 2>::zeros(),
            Matrix::<f32, 4, 2>::zeros()
        );
        assert_eq!(
            m![[1., 2.], [3., 4.]] + &m![[-1., -2.], [-3., -4.]],
            Matrix::zeros()
        );
        assert_eq!(
            &m![[0.5, 1., 1.5], [2., 2.5, 3.]] + m![[2.5, 2., 1.5], [1., 0.5, 0.]],
            Matrix::full(3.)
        );
        assert_eq!(&m![[1., 2.5, 0.]] + &m![[3., -4., 0.]], m![[4., -1.5, 0.]]);
    }

    #[test]
    fn test_sub() {
        assert_eq!(
            Matrix::<f32, 4, 2>::zeros() - Matrix::<f32, 4, 2>::zeros(),
            Matrix::<f32, 4, 2>::zeros()
        );
        assert_eq!(
            m![[1., 2.], [3., 4.]] - &m![[1., 2.], [3., 4.]],
            Matrix::zeros()
        );
        assert_eq!(
            &m![[0.5, 1., 1.5], [2., 2.5, 3.]] - m![[1.5, 2., 2.5], [3., 3.5, 4.]],
            Matrix::full(-1.)
        );
        assert_eq!(&m![[1., 2.5, 0.]] - &m![[3., -4., 0.]], m![[-2., 6.5, 0.]]);
    }

    #[test]
    fn test_scalar_mul() {
        assert_eq!(Matrix::<f32, 4, 2>::zeros() * 7., Matrix::zeros());
        assert_eq!(m![[1., 2.]] * &3., m![[3., 6.]]);
        assert_eq!(&m![[1.], [2.]] * -2.5, m![[-2.5], [-5.]]);
        assert_eq!(&Matrix::<f32, 4, 2>::full(2.5) * &2.5, Matrix::full(6.25));
    }
}
