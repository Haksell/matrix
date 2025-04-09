pub trait IsClose {
    fn is_close(&self, rhs: &Self) -> bool;
}

macro_rules! impl_is_close {
    ($t:ty) => {
        impl IsClose for $t {
            fn is_close(&self, rhs: &Self) -> bool {
                (self - rhs).abs() < 1e-7
            }
        }

        impl<const N: usize> IsClose for crate::Vector<$t, N> {
            fn is_close(&self, rhs: &Self) -> bool {
                (0..N).all(|i| self[i].is_close(&rhs[i]))
            }
        }

        impl<const H: usize, const W: usize> IsClose for crate::Matrix<$t, H, W> {
            fn is_close(&self, rhs: &Self) -> bool {
                (0..H).all(|y| (0..W).all(|x| self[(y, x)].is_close(&rhs[(y, x)])))
            }
        }
    };
}

impl_is_close!(f32);
impl_is_close!(f64);
