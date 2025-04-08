pub trait Field: Copy + Default + PartialEq {}

impl Field for f32 {}

impl Field for f64 {}
