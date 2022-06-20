from enum import Enum
from pydantic import BaseModel, AnyUrl


class ProviderEnum(str, Enum):
    GitHTTPS = "GitHTTPS"
    GitHTTP = "GitHTTP"
    Github = "Github"
    Gitlab = "Gitlab"
    AzureDevops = "AzureDevops"
    S3 = "S3"
    FTP = "FTP"
    KeyBase = "KeyBase"
    SMB = "SMB"
    VAULT = "Vault"


class RepositoryConfig(BaseModel):
    provider:  ProviderEnum
    url: AnyUrl
    authentication: bool


class DevryConfig(BaseModel):

    EnvConfig: RepositoryConfig
    SecretsConfig: RepositoryConfig
