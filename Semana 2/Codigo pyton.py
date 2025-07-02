import json

# Data containing student academic records.
# This JSON-like structure holds information about students, their semesters,
# subjects, credits, and performance in assignments, exams, and attendance.
data = {
    "students": [
        {
            "id": "S001",
            "name": "Alice",
            "semesters": [
                {
                    "term": "Fall 2023",
                    "subjects": [
                        {"name": "Math", "credits": 4,
                         "performance": {"assignments": 80, "exams": 70, "attendance": 85}},
                        {"name": "Physics", "credits": 3,
                         "performance": {"assignments": 90, "exams": 60, "attendance": 70}}
                    ]
                }
            ]
        },
        {
            "id": "S002",
            "name": "Bob",
            "semesters": [
                {
                    "term": "Fall 2023",
                    "subjects": [
                        {"name": "Math", "credits": 4,
                         "performance": {"assignments": 85, "exams": 75, "attendance": 90}},
                        {"name": "English", "credits": 2,
                         "performance": {"assignments": 95, "exams": 82, "attendance": 60}}
                    ]
                }
            ]
        }
    ]
}


def calculate_final_grade(performance: dict) -> float:
    """
    Calculates a subject's final grade as a weighted average.
    Weights are: 30% assignments, 50% exams, 20% attendance.

    Args:
        performance (dict): A dictionary containing performance scores for 'assignments',
                            'exams', and 'attendance'.

    Returns:
        float: The calculated final grade for the subject, or 0.0 if data is missing or invalid.
    """
    # Validate input keys and types for robustness.
    try:
        # Using .get() with a default value handles missing keys gracefully.
        # Converting to float ensures numeric operations and handles potential string numbers.
        assignments = float(performance.get('assignments', 0))
        exams = float(performance.get('exams', 0))
        attendance = float(performance.get('attendance', 0))
    except (TypeError, ValueError):
        # Return 0.0 if performance data is not numeric or cannot be converted.
        return 0.0

    # Apply the specified weights for final grade calculation.
    return (0.3 * assignments) + (0.5 * exams) + (0.2 * attendance)


def calculate_gpa(subjects: list) -> tuple[float, float, float]:
    """
    Calculates the GPA for a list of subjects, along with their total credits and total weighted grades.

    Args:
        subjects (list): A list of subject dictionaries, each containing 'name',
                         'credits', and 'performance'.

    Returns:
        tuple[float, float, float]: A tuple containing:
                                    - The calculated GPA (on a 4.0 scale).
                                    - Total credits accumulated from these subjects.
                                    - Total weighted grades accumulated from these subjects.
                                    Returns (0.0, 0.0, 0.0) if no valid subjects or credits are found.
    """
    total_weighted_grades = 0.0
    total_credits = 0.0

    for subject in subjects:
        # Basic validation to ensure the subject is a dictionary and has required keys.
        if not isinstance(subject, dict) or 'credits' not in subject or 'performance' not in subject:
            # Skip malformed subjects to prevent errors.
            continue

        try:
            credits = float(subject['credits'])
            # Ensure credits are non-negative, as negative credits don't make sense.
            if credits < 0:
                continue
        except (TypeError, ValueError):
            # Skip subjects if credits are not numeric or cannot be converted.
            continue

        # Calculate the final grade for the current subject.
        final_grade = calculate_final_grade(subject['performance'])
        # Store the calculated final grade back into the subject dictionary for later use (e.g., in transcript generation).
        subject['final_grade'] = final_grade

        total_weighted_grades += final_grade * credits
        total_credits += credits

    # Avoid division by zero if there are no subjects or total credits are zero.
    if total_credits == 0:
        return 0.0, 0.0, 0.0

    # Calculate GPA on a 4.0 scale using the formula (weighted grade / 100) * 4.
    gpa = (total_weighted_grades / total_credits) / 100 * 4
    return gpa, total_credits, total_weighted_grades


def generate_transcript(student: dict):
    """
    Generates and prints the academic transcript for a given student.
    This includes GPA per semester, cumulative GPA, and identifies academic honors for GPAs >= 3.7.

    Args:
        student (dict): A dictionary containing student details and their academic records over semesters.
    """
    # Validate the basic structure of the student dictionary.
    if not isinstance(student, dict) or 'name' not in student or 'id' not in student or 'semesters' not in student:
        print("Error: Invalid student data structure provided. Skipping transcript generation.")
        return

    print(f"Transcript for {student['name']} (ID: {student['id']})")

    cumulative_weighted_grades = 0.0
    cumulative_credits = 0.0

    for semester in student['semesters']:
        # Validate the basic structure of each semester.
        if not isinstance(semester, dict) or 'term' not in semester or 'subjects' not in semester:
            print(
                f"Warning: Skipping malformed semester data for {student['name']} in term {semester.get('term', 'Unknown Term')}.")
            continue  # Skip malformed semesters

        print(f"Term: {semester['term']}")

        # Calculate GPA, credits, and weighted grades for the current semester.
        semester_gpa, semester_credits, semester_weighted_grades = calculate_gpa(semester['subjects'])

        # Optimize: Directly use semester_weighted_grades from calculate_gpa result
        # instead of re-summing (addressing minor efficiency issue).
        cumulative_weighted_grades += semester_weighted_grades
        cumulative_credits += semester_credits

        # Determine if academic honors are achieved for the current semester.
        honors = " with Honors" if semester_gpa >= 3.7 else ""
        print(f"GPA for this semester: {semester_gpa:.2f}{honors}")

    # Calculate cumulative GPA, avoiding division by zero if no credits accumulated.
    cumulative_gpa = (cumulative_weighted_grades / cumulative_credits) / 100 * 4 if cumulative_credits > 0 else 0.0

    # Determine if academic honors are achieved based on cumulative GPA.
    honors = " with Honors" if cumulative_gpa >= 3.7 else ""
    print(f"Cumulative GPA: {cumulative_gpa:.2f}{honors}\n")


# Main execution block.
# This ensures that the code runs when executed as a script but not when imported as a module,
# adhering to Python best practices for modularity.
if __name__ == "__main__":
    # Basic validation for the overall data structure to ensure 'students' list exists.
    if not isinstance(data, dict) or "students" not in data or not isinstance(data["students"], list):
        print("Error: Invalid main data structure. Expected 'students' list not found.")
    else:
        # Iterate through each student record in the data and generate their transcript.
        for student_record in data['students']:
            generate_transcript(student_record)