from services.auth_service import AuthService

aaa = AuthService.make_access_token("FFF", "FFF")
aa = AuthService.verify_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IkZGRiIsImZ1bGxOYW1lIjoiRkZGIn0.mh5Y82d1Fav2Pk0dRyZdLoCE8nHBd3WTzwdL6OrelHk')
print("")