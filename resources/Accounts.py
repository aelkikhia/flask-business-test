from flask_restful import Resource


class AccountList(Resource):

    def get(self, name):
        accounts_list = [{
            "id": 3891648,
            "account_description": "R5 Checking XXXXXX1014 $184.44",
            "display_order": 0,
            "balance": "$184.44",
            "raw_balance": 184.44,
            "is_external": True,
            "is_active": True,
            },
            {
            "id": 3891653,
            "account_description": "Individual Daily Investment XXXXXX2886 $14,670.80",
            "display_order": 0,
            "balance": "$14,670.80",
            "raw_balance": 14670.8,
            "is_external": False,
            "is_active": False
            },
            {
            "id": 3891655,
            "account_description": "Employee Performance XXXXXX6662 $133.33",
            "display_order": 0,
            "balance": "$133.33",
            "raw_balance": 133.33,
            "is_external": True,
            "is_active": False
            },
            {
            "id": 3846279,
            "account_description": "bills XXXXXX2221 $2,878.06",
            "display_order": 2,
            "balance": "$2,878.06",
            "raw_balance": 2878.06,
            "is_external": False,
            "is_active": False
            },
            {
            "id": 3846281,
            "account_description": "UMB Access Checking XXXXXX9786 $0.00",
            "display_order": 3,
            "balance": "$0.00",
            "raw_balance": 0.0,
            "is_external": True,
            "is_active": False
            }
        ]

        return {'data': [account for account in accounts_list]}
