import numpy as np

def calculate_vector_properties(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    
    if norm_a == 0 or norm_b == 0:
        print("Нөлдік векторларға бұрыш анықталмаған.")
        return dot_product, None

    cos_theta = dot_product / (norm_a * norm_b)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    
    angle_rad = np.arccos(cos_theta)
    angle_deg = np.degrees(angle_rad)

    return dot_product, angle_deg

vector_A = np.array([1, 2, 3])
vector_B = np.array([4, -1, 5])

scalar_product, angle_in_degrees = calculate_vector_properties(vector_A, vector_B)

print(f"Вектор A: {vector_A}")
print(f"Вектор B: {vector_B}")
print("-" * 30)

if angle_in_degrees is not None:
    print(f"1. Скаляр көбейтінді (A ⋅ B): {scalar_product}")

    print(f"2. Векторлар арасындағы бұрыш: {angle_in_degrees:.2f}°")
else:
    print(f"1. Скаляр көбейтінді (A ⋅ B): {scalar_product}")

    print("2. Бұрышты есептеу мүмкін емес (Нөлдік вектор бар).")
