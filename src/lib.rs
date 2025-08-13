#![no_std]

mod field;
mod matrix;
mod vector;

pub use {
    field::{Field, IsClose},
    matrix::Matrix,
    vector::Vector,
};

use core::ops::{Add, Mul};

pub fn linear_combination<K: Field, const N: usize>(
    vecs: &[Vector<K, N>],
    coefs: &[K],
) -> Vector<K, N> {
    debug_assert_eq!(vecs.len(), coefs.len());
    Vector::from(core::array::from_fn(|i| {
        core::iter::zip(vecs, coefs)
            .map(|(v, c)| v[i] * c)
            .sum::<K>()
    }))
}

pub fn lerp<V: Mul<f32, Output = V> + Add<V, Output = V>>(u: V, v: V, t: f32) -> V {
    debug_assert!(0. <= t && t <= 1.); // the subject is unclear
    u * (1. - t) + v * t
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_linear_combination() {
        assert_eq!(
            linear_combination(
                &[v![1., 0., 0.], v![0., 1., 0.], v![0., 0., 1.]],
                &[10., -2., 0.5]
            ),
            v![10., -2., 0.5]
        );

        assert_eq!(
            linear_combination(&[v![1., 2., 3.], v![0., 10., -100.]], &[10., -2.]),
            v![10., 0., 230.]
        );
    }

    #[test]
    #[should_panic]
    fn test_linear_combination_invalid() {
        linear_combination(
            &[Vector::<f32, 2>::zeros(), Vector::<f32, 2>::ones()],
            &[15., 27., 42.],
        );
    }

    #[test]
    fn test_lerp() {
        assert_eq!(lerp(0., 1., 0.), 0.);
        assert_eq!(lerp(0., 1., 0.5), 0.5);
        assert_eq!(lerp(0., 1., 1.), 1.);
        assert!(lerp(21., 42., 0.3).is_close(&27.3));
        assert!(lerp(v![2., 1.], v![4., 2.], 0.3).is_close(&v![2.6, 1.3]));
        assert_eq!(
            lerp(
                Matrix::from([[2., 1.], [3., 4.]]),
                Matrix::from([[20., 10.], [30., 40.]]),
                0.5
            ),
            m![[11., 5.5], [16.5, 22.]]
        )
    }

    #[test]
    #[should_panic]
    fn test_lerp_invalid() {
        assert_eq!(lerp(0., 1., 1.1), 0.);
    }
}
