use crate::field::Field;

#[derive(Clone, Debug, PartialEq)]
pub struct Matrix<K: Field, const H: usize, const W: usize> {
    values: [[K; W]; H],
}

impl<K: Field, const H: usize, const W: usize> Matrix<K, H, W> {
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

impl<K: Field, const H: usize, const W: usize> Default for Matrix<K, H, W> {
    fn default() -> Self {
        Self {
            values: [[K::default(); W]; H],
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_default() {
        assert_eq!(
            Matrix::<f32, 2, 3>::default().values,
            [[0., 0., 0.], [0., 0., 0.]]
        );
    }

    #[test]
    fn test_shape() {
        let m = Matrix::<f32, 2, 3>::default();
        assert_eq!(m.height(), 2);
        assert_eq!(m.width(), 3);
        assert_eq!(m.shape(), (2, 3));
    }

    #[test]
    fn test_is_square() {
        assert!(!Matrix::<f32, 2, 3>::default().is_square());
        assert!(Matrix::<f32, 6, 6>::default().is_square());
    }
}
