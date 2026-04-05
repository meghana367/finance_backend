from fastapi import Header, HTTPException

def verify_role(role_required: str):
    def role_checker(x_user_role: str = Header(..., description="Role: Admin, Analyst, or Viewer")):
        # Admin bypasses all checks
        if x_user_role == "Admin":
            return x_user_role
        
        # Logic for specific access
        if role_required == "Analyst" and x_user_role == "Analyst":
            return x_user_role
            
        if x_user_role != role_required:
            raise HTTPException(
                status_code=403, 
                detail=f"Access denied. Role '{role_required}' or 'Admin' required."
            )
        return x_user_role
    return role_checker