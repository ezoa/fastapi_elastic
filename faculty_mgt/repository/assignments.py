from fastapi.encoders import jsonable_encoder
from typing import Dict, Any
from faculty_mgt.models.data.facultydb import faculty_assignments_tbl, student_bin_tbl
from faculty_mgt.models.data.faculty import Assignment, StudentBin
from collections import namedtuple

class AssignmentRepository:

    def insert_assignment(self, assignment:Assignment)-> bool:
        try:
            faculty_assignments_tbl[assignment.assgn_id]=assignment
        
        except:
            return False
        return True
    



    def update_assignment(self, assgn_id:int, details:Dict[str, Any])->bool:
        try:
            assignment= faculty_assignments_tbl[assgn_id]
            assignment_enc=jsonable_encoder(assignment)
            assignment_dict= dict(assignment_enc)
            assignment_dict.update(details)
            faculty_assignments_tbl[assgn_id]=namedtuple("Assignment",assignment_dict.keys())(*assignment_dict.values())
        except: 
           return False 
        return True


    def delete_assignment(self,assgn_id:int)-> bool:

        try:
            del faculty_assignments_tbl[assgn_id]

        except:
            return False
        return True
    

    def get_all_assignment_tbl(sel):

        return faculty_assignments_tbl
    

class AssignmentSubmissionRepository: 
    
    def create_bin(self, stud_id:int, bin_id:int, faculty_id:int): 
        try:
            student_bin = StudentBin(bin_id=bin_id, faculty_id=faculty_id, stud_id=stud_id)
            student_bin_tbl[bin_id]=student_bin
        except: 
            return False 
        return True 
    
    def insert_submission(self, bin_id:int, assignment:Assignment): 
        try:
            student_bin:StudentBin = student_bin_tbl[bin_id]
            student_bin.assignment.append(assignment)
        except: 
            return False 
        return True 
    
    def delete_submission(self, bin_id:int, assignment:Assignment ): 
        find_assignment = [work for work in student_bin_tbl[bin_id].assignment if work.assgn_id==assignment.assgn_id] 
        if len(find_assignment) == 0: 
            return False 
        else: 
            assignment = find_assignment[0]
            student_bin_tbl[bin_id].assignment.remove(assignment)
            return True
        
    def get_submissions(self, bin_id:int): 
        return student_bin_tbl[bin_id]
    

# # Example usage:
# repo = AssignmentRepository()

# # Inserting an assignment
# assignment1 = Assignment(1, "First Assignment", "Details of the first assignment")
# repo.insert_assignment(assignment1)

# # Updating an assignment
# update_details = {
#     "title": "Updated Assignment Title",
#     "details": "Updated Assignment Details"
# }
# repo.update_assignment(1, update_details)

# # Printing the contents of faculty_assignments_tbl
# print("Current faculty_assignments_tbl:")
# for key, value in faculty_assignments_tbl.items():
#     print(f"Assignment ID: {key}, Title: {value.title}, Details: {value.details}")
