use std::ops::Add;

pub trait Field: Add<Self, Output = Self> + Copy + Default + PartialEq {}

impl Field for f32 {}

impl Field for f64 {}
