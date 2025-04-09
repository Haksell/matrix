mod field;
mod matrix;
mod vector;

pub use {field::Field, matrix::Matrix, vector::Vector};

pub fn linear_combination<K: Field, const N: usize>(
    vecs: &[Vector<K, N>],
    coefs: &[K],
) -> Vector<K, N> {
    assert_eq!(vecs.len(), coefs.len());
    Vector::from(core::array::from_fn(|i| {
        std::iter::zip(vecs, coefs)
            .map(|(v, c)| v[i] * c)
            .sum::<K>()
    }))
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
}
