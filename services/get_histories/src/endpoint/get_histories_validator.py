from utils.utils import validate_parameters

get_histories_body_schema = {}

class GetHistoriesValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.form, get_histories_body_schema)
        return body_validation_errors