# 1. Create a matrix of student scores
import numpy as np

np.random.seed(42)
scores = np.random.randint(50, 100, size=(10, 5))
subjects = ["Math", "Physics", "Chemistry", "English", "History"]
students = [f"Student_{i+1}" for i in range(10)]
print("--- Bảng điểm (scores) ---")
print(scores)
print("\n--- Danh sách Sinh viên (students) ---")
print(students)
print("\n--- Danh sách Môn học (subjects) ---")
print(subjects)

# 1. What is the shape, size, and data type of the scores array?
print(f"Shape: {scores.shape}")
print(f"Size: {scores.size}")
print(f"Data Type: {scores.dtype}")

# 2. Print all the scores of Student_x (ex: student_3)
print("Scores of Student_2:")
print(scores[1, :])
print("\n")
print("=="*20)
# 3. Print all the scores of subject Physics
print("Scores of Physics:")
print(scores[:, 1])
print("\n")
print("=="*20)

# 4. Display the 3x3 subarray of the top-left corner of the matrix
print("Top-left 3x3 subarray:")
print(scores[:3, :3])
print("\n")
print("=="*20)
# 5. Change the score of Student_1 in Math to 95
print(f"Điểm cũ của Student_1 môn Math: {scores[0, 0]}")
scores[0, 0] = 95
print(f"Điểm mới của Student_1 môn Math: {scores[0, 0]}")
print("\n")
print("=="*20)

# Section 2: Statistical Computation
# 1. Compute the average score of each student.
avg_scores_students = np.mean(scores, axis=1)
print(f"Điểm TB của mỗi sinh viên:\n {avg_scores_students}")
print("\n")
print("=="*20)

# 2. Compute the average score of each subject.
avg_scores_subjects = np.mean(scores, axis=0)
print(f"Điểm TB của mỗi môn học:\n {avg_scores_subjects}")
print("\n")
print("=="*20)

# 3. Find the highest and lowest scores in the entire dataset.
highest_score = np.max(scores) # Hoặc scores.max()
lowest_score = scores.min()  
print(f"Điểm cao nhất: {highest_score}")
print(f"Điểm thấp nhất: {lowest_score}")
print("\n")
print("=="*20)

# 4. Identify the student with the highest overall average.
# Tận dụng mảng avg_scores_students từ câu 1
best_student_index = np.argmax(avg_scores_students)
best_student_name = students[best_student_index]
print(f"SV có điểm TB cao nhất: {best_student_name} (Index: {best_student_index})")
print("\n")
print("=="*20)

# 5. Identify the subject with the lowest class average.
worst_subject_index = np.argmin(avg_scores_subjects)
worst_subject_name = subjects[worst_subject_index]
print(f"Môn học có điểm TB thấp nhất: {worst_subject_name} (Index: {worst_subject_index})")
print("\n")
print("=="*20)

# Section 3: Conditional Filtering
# 1. List all students whose average score ≥ 80.
check_gt_80 = avg_scores_students >= 80
students_gt_80 = np.array(students)[check_gt_80]

print(f"Mask (True/False): {check_gt_80}")
print(f"SV có điểm TB >= 80: {students_gt_80}")
print("\n")
print("=="*20)
# 2. Find all scores that are below 60 and replace them with 60 (to simulate a minimum passing mark).

scores[scores < 60] = 60 
print("Bảng điểm sau khi cập nhật:\n", scores)
print("==" * 20)
# Section 4: Combining & Sorting
# 1. Combine students and their average scores into one array using np.column_stack().


combined_array = np.column_stack((students, avg_scores_students))
print("Mảng kết hợp (Student và Điểm TB):\n", combined_array)
print(f"Kiểu dữ liệu mảng kết hợp: {combined_array.dtype}")
print("\n")
print("==" * 20)
# 2. Sort this combined array by average score (descending).
sorted_indices_asc = np.argsort(avg_scores_students)
# print("Index sắp xếp (tăng dần):", sorted_indices_asc)
sorted_indices_desc = sorted_indices_asc[::-1]
print("Index sắp xếp (giảm dần):", sorted_indices_desc)

# 3. Display the top 3 students.

top_3_indices = sorted_indices_desc[:3]
print("Index của Top 3:", top_3_indices)
print("\n--- Top 3 Sinh viên ---")
top_3_students_names = np.array(students)[top_3_indices]
top_3_students_scores = avg_scores_students[top_3_indices]
for i in range(len(top_3_students_names)):
    print(f"Hạng {i+1}: {top_3_students_names[i]} (Điểm TB: {top_3_students_scores[i]:.2f})")
    
# 4. Compute the class median score and compare it with the mean — which is higher?
# 1. Tính Mean (Trung bình cộng) của toàn bộ 50 điểm
class_mean = np.mean(scores)

# 2. Tính Median (Trung vị) của toàn bộ 50 điểm
class_median = np.median(scores)

print(f"\n--- So sánh Mean và Median ---")
print(f"Điểm trung bình (Mean) toàn lớp: {class_mean:.2f}")
print(f"Điểm trung vị (Median) toàn lớp: {class_median:.2f}")

# 3. So sánh
if class_mean > class_median:
    print("=> Mean (Trung bình cộng) cao hơn Median (Trung vị).")
elif class_median > class_mean:
    print("=> Median (Trung vị) cao hơn Mean (Trung bình cộng).")
else:
    print("=> Mean và Median bằng nhau.")