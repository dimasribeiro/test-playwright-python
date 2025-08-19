from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.post_livraria_client import PostLivrariaCLient
from pytests.support.api_utils import ApiUtils
from pytests.clients.common import Common
from pytests.clients.delete_livraria_client import DeleteLivrariaClient
from pytests.schemas.delete_livros_schema import *
from pytests.examples.examples_test_delete_livraria import *
import json

@pytest.mark.crud_livros
def test_delete_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = PostLivrariaCLient.post_livros(payload)
    Common.validate_response(response, 201)
    response_json = json.loads(response['body'])
    id = response_json['id']
    response = DeleteLivrariaClient.delete_livros(id)
    Common.validate_response(response, 200)
    ApiUtils.validate_json_schema(response, delete_schema)

@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", examples_delete_livraria_invalid_values)
def test_delete_livro_invalid_values(value, code):
    value_change = Common.values_change(value)
    response = DeleteLivrariaClient.delete_livros(value_change)
    Common.validate_response(response, code)
