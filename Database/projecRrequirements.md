# FOR STORING ATTENDANCE DETAILS
### For Students
|  roll  |    date    |  status |
|:------:|:----------:|:-------:|
| 121001 | 14-09-2024 | Present |
| 121002 | 14-09-2024 | Present |


<br>

# FOR STORING STUDENT & FACULTY DETAILS
## For New Tables
### For Students
- Create a new table for student details
    - `Student ID (auto-generated primary key)`
    - `Student Roll Number`
    - `Student First Name`
    - `Student Last Name`
- Name the table as `{dept_name}_p{passout_year}_students` (eg: `cse_p2020_students`)

| s_id | roll   | firstname | lastname |
|:----:|:------:|:---------:|:--------:|
| 1    | 121001 | _John_    | _Doe_    |
| 2    | 121002 | _Jane_    | _Doe_    |

### For Faculties
- Create a new table for faculty details
    - `Faculty ID (auto-generated primary key)`
    - `Faculty Serial Number`
    - `Faculty First Name`
    - `Faculty Last Name`
    - `Faculty Department`
- Name the table as `faculties`

| f_id | f_serial | firstname | lastname | department |
|:----:|:--------:|:---------:|:--------:|:----------:|
|   1  |   90101  |   _John_  |  _Smith_ |     CSE    |
|   2  |   90102  |  _Olivia_ |  _Smith_ |     ECE    |
|      |          |           |          |            |

<br><br>

## For Already Existing Tables
### For Students
- `Insert new students into the database - for new admissions`
- `Delete students from the database - for students who have left`
- `Update student details - for students who have changed their details`
- `Query student details - for students who want to know their details`
- `Query students based on their department - for faculties who want to know the students in their department`

### For Faculties
- `Insert new faculties into the database - for new faculties`
- `Delete faculties from the database - for faculties who have left`
- `Update faculty details - for faculties who have changed their details`
- `Query faculty details - for faculties who want to know their details`
- `Query faculties based on their department - for students who want to know the faculties in their department`

