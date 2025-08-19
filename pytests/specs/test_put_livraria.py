from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.put_livraria_client import PutLivrariaCLient
from pytests.support.api_utils import ApiUtils
from pytests.schemas.put_livros_schema import *
from pytests.clients.common import *
from pytests.examples.examples_test_put_livraria import *

@pytest.mark.crud_livros
def test_put_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = PutLivrariaCLient.put_livros(payload, 2)
    Common.validate_response(response, 200)
    ApiUtils.validate_json_schema(response, put_schema)

@pytest.mark.crud_livros
@pytest.mark.parametrize("payload, code", examples_put_livraria_invalid_payload)
def test_put_livros_invalid_payload(payload, code):
    payload = Common.incorrect_payload(payload)
    ApiUtils.payload_parse(payload)
    response = PutLivrariaCLient.put_livros(payload, 2)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", examples_put_livraria_invalid_values)
def test_put_livros_invalid_values(field, value, code):
    payload = payload_post_livros()
    payload = Common.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse(payload)
    response = PutLivrariaCLient.put_livros(payload, 2)
    Common.validate_response(response, code)

@pytest.mark.crud_livros
@pytest.mark.parametrize("field, code", examples_put_livraria_no_fields)
def test_put_livros_no_fields(field, code):
    payload = payload_post_livros()
    payload = Common.remove_fields_payload(payload, field)
    ApiUtils.payload_parse(payload)
    response = PutLivrariaCLient.put_livros(payload, 2)
    Common.validate_response(response, code)

@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", examples_put_id_livraria_invalid_values)
def test_put_id_livro_invalid_values(value, code):
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    values_change = Common.values_change(value)
    response = PutLivrariaCLient.put_livros(payload, values_change)
    Common.validate_response(response, code)

