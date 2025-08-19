get_schema = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "integer"
      },
      "nome": {
        "type": "string"
      },
      "autor": {
        "type": "string"
      },
      "data_publicacao": {
        "type": "string",
        "format": "date-time"
      },
      "qtde_paginas": {
        "type": "integer"
      },
      "created_on": {
        "type": "string",
        "format": "date-time"
      },
      "update_at": {
        "type": ["string", "null"],
        "format": "date-time"
      }
    },
    "required": ["id", "nome", "autor", "data_publicacao", "qtde_paginas", "created_on"]
  }
}