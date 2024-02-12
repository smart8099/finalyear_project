def is_physician(user):
    return user.user_type == 'PHYSICIAN'

def is_nurse(user):
    return user.user_type == 'NURSE'

def is_lab_technician(user):
    return user.user_type == 'LAB_TECHNICIAN'

def is_record_manager(user):
    return  user.user_type == 'RECORD_MANAGER'

def is_hyperx_admin(user):
    return user.user_type == 'HOSPITAL_REGISTRAR'


def is_record_manager_or_hospital_registrar(user):
    return  user.user_type ==  'RECORD_MANAGER' or user.user_type == 'HOSPITAL_REGISTRAR'
