from .get_histories_validator import GetHistoriesValidator
from .get_histories_flow import GetHistoriesFlow


class GetHistories:

    def __call__(self, request):

        get_histories_validation = GetHistoriesValidator()
        get_histories_validation_errors = get_histories_validation(request)
        if get_histories_validation_errors:
            return get_histories_validation_errors

        get_histories_flow = GetHistoriesFlow()
        return get_histories_flow()

            
