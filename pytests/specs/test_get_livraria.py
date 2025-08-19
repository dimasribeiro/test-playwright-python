from pytests.support.hooks import *
from pytests.clients.get_livraria_client import GetLivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.schemas.get_livros_schema import *
from pytests.clients.common import Common
from pytests.examples.examples_test_get_livraria import *

@pytest.mark.crud_livros
def test_get_all_livro():
    response = GetLivrariaClient.get_livros()
    Common.validate_response(response, 200)

@pytest.mark.crud_livros
def test_get_id_livro():
    response = GetLivrariaClient.get_livros(10)
    Common.validate_response(response, 200)
    ApiUtils.validate_json_schema(response, get_schema)

@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", examples_get_livraria_invalid_values)
def test_get_livro_invalid_values(value, code):
    value_change = Common.values_change(value)
    response = GetLivrariaClient.get_livros(value_change)
    Common.validate_response(response, code)




