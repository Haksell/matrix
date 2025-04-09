use crate::field::Field;

#[derive(Clone, Debug, PartialEq)]
pub struct Matrix<K: Field, const H: usize, const W: usize> {
    values: [[K; W]; H],
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_constructors() {
        assert_eq!(
            Matrix::from([[1., 2.], [3.14, 4.2]]).values,
            [[1., 2.], [3.14, 4.2]]
        );
        assert_eq!(
            Matrix::<f32, 3, 2>::zeros().values,
            [[0., 0.], [0., 0.], [0., 0.]]
        );
        assert_eq!(
            Matrix::<f32, 2, 3>::ones(),
            Matrix::from([[1., 1., 1.], [1., 1., 1.]])
        );
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
}
