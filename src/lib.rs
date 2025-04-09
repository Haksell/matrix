mod field;
mod matrix;
mod vector;

pub use {field::Field, matrix::Matrix, vector::Vector};

// pub fn linear_combination<K: Field, const N: usize>(
//     vecs: &[Vector<K, N>],
//     coefs: &[K],
// ) -> Vector<K, N> {
//     assert_eq!(vecs.len(), coefs.len());
//     let values = core::array::from_fn(|i| {
//         std::iter::zip(vecs, coefs)
//             .map(|(v, c)| v.values[i] * c)
//             .sum::<K>()
//     });
//     Vector::from(values)
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn test_linear_combination() {}

//     #[test]
//     #[should_panic]
//     fn test_linear_combination_invalid() {
//         linear_combination(
//             &[Vector::<f32, 2>::zeros(), Vector::<f32, 2>::ones()],
//             &[15., 27., 42.],
//         );
//     }
// }
