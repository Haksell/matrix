use core::{
    iter::Sum,
    ops::{Add, Mul, Sub},
};

pub trait IsClose {
    fn is_close(&self, rhs: &Self) -> bool;
}

pub trait Field:
    Copy
    + PartialEq
    + Add<Self, Output = Self>
    + for<'a> Add<&'a Self, Output = Self>
    + Sub<Self, Output = Self>
    + for<'a> Sub<&'a Self, Output = Self>
    + Mul<Self, Output = Self>
    + for<'a> Mul<&'a Self, Output = Self>
    + Sum<Self>
    + for<'a> Sum<&'a Self>
    + IsClose
{
    fn zero() -> Self;
    fn one() -> Self;
    fn inverse(self) -> Self;
}

macro_rules! impl_field {
    ($field:ty) => {
        impl IsClose for $field {
            fn is_close(&self, rhs: &Self) -> bool {
                (self - rhs).abs() < 1e-7
            }
        }

        impl<const N: usize> IsClose for crate::Vector<$field, N> {
            fn is_close(&self, rhs: &Self) -> bool {
                (0..N).all(|i| self[i].is_close(&rhs[i]))
            }
        }

        impl<const H: usize, const W: usize> IsClose for crate::Matrix<$field, H, W> {
            fn is_close(&self, rhs: &Self) -> bool {
                (0..H).all(|y| (0..W).all(|x| self[(y, x)].is_close(&rhs[(y, x)])))
            }
        }

        impl Field for $field {
            fn zero() -> Self {
                0.
            }

            fn one() -> Self {
                1.
            }

            fn inverse(self) -> Self {
                Self::one() / self
            }
        }
    };
}

impl_field!(f32);
impl_field!(f64);
