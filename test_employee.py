from employee import employee_info
def test_employee_info():
    expected_output = (
        "Employee Name: Rahul\n"
        "Employee ID: EMP1024\n"
        "Department: IT\n"
        "salary: 55000"
    )
    assert employee_details("Alice","EMP1024","IT",55000) == expectd_output
