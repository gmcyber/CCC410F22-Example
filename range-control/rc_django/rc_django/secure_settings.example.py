import ldap 
from django_auth_ldap.config import LDAPSearch, NestedActiveDirectoryGroupType 
# Binding and connection options 

# Baseline configuration.
#AUTH_LDAP_SERVER_URI = "ldap://domaincontroller"

#ldaps
AUTH_LDAP_GLOBAL_OPTIONS = {ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER}
AUTH_LDAP_SERVER_URI = "ldaps://domaincontroller"


AUTH_LDAP_BIND_DN = "ldap user bind dn"
AUTH_LDAP_BIND_PASSWORD = "password goes here"

AUTH_LDAP_CONNECTION_OPTIONS = { ldap.OPT_DEBUG_LEVEL: 1, ldap.OPT_REFERRALS: 0, } 


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"django_auth_ldap": {"level": "DEBUG", "handlers": ["console"]}},
}

# User and group search objects and types 
AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=accounts,OU=cyber,DC=cyber,DC=local", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)") 
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("OU=groups,OU=cyber,DC=cyber,DC=local", ldap.SCOPE_SUBTREE, "(objectClass=group)") 
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType() 
# Cache settings 
AUTH_LDAP_CACHE_GROUPS = True 
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300 
# What to do once the user is authenticated 
AUTH_LDAP_USER_ATTR_MAP = { "username": "sAMAccountName", "email": "mail" } 
AUTH_LDAP_USER_FLAGS_BY_GROUP = { "is_staff": ["CN to the group you want to have access to the admin site"], "is_superuser": ["identify the super users with a CN to the group"] } 
AUTH_LDAP_FIND_GROUP_PERMS = True 
# The backends needed to make this work. 
AUTHENTICATION_BACKENDS = ( 'django_auth_ldap.backend.LDAPBackend','django.contrib.auth.backends.ModelBackend') 