use std::ops::{Add, Sub};

pub trait Field: Copy + PartialEq + Add<Self, Output = Self> + Sub<Self, Output = Self> {
    fn zero() -> Self;
    fn one() -> Self;
    fn inverse(self) -> Self;
}

macro_rules! impl_field {
    ($field:ty) => {
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
