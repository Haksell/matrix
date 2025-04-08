use crate::field::Field;

#[derive(Clone, Debug, PartialEq)]
pub struct Vector<K: Field, const N: usize> {
    values: [K; N],
}

impl<K: Field, const N: usize> Default for Vector<K, N> {
    fn default() -> Self {
        Self {
            values: [K::default(); N],
        }
    }
}

impl<K: Field, const N: usize> Vector<K, N> {
    pub const fn len(&self) -> usize {
        N
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_default() {
        assert_eq!(Vector::<f32, 3>::default().values, [0., 0., 0.]);
    }

    #[test]
    fn test_len() {
        assert_eq!(Vector::<f32, 42>::default().len(), 42);
    }
}
