import requests
from requests.structures import CaseInsensitiveDict
from urllib import parse
import requests
from requests.structures import CaseInsensitiveDict
from urllib import parse
import urllib
import json


class Airbnb:
    def __init__(self):
        headers = CaseInsensitiveDict()
        headers["authority"] = "www.airbnb.com.au"
        headers["device-memory"] = "8"
        headers["x-airbnb-graphql-platform-client"] = "minimalist-niobe"
        headers["x-csrf-token"] = "V4$.airbnb.com.au$hnpNs2fu9-E$M7btLkHrQ0LvW_zbGGGFUMySzj0MeiFTi28beQam9Hc="
        headers["x-airbnb-api-key"] = "d306zoyjsyarp7ifhu67rjxn52tv0t20"
        headers["sec-ch-ua-mobile"] = "?0"
        headers["x-csrf-without-token"] = "1"
        headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        headers["viewport-width"] = "1142"
        headers["content-type"] = "application/json"
        headers["x-niobe-short-circuited"] = "true"
        headers["x-airbnb-supports-airlock-v2"] = "true"
        headers["dpr"] = "1"
        headers["ect"] = "4g"
        headers["x-airbnb-graphql-platform"] = "web"
        headers["accept"] = "*/*"
        headers["sec-fetch-site"] = "same-origin"
        headers["sec-fetch-mode"] = "cors"
        headers["sec-fetch-dest"] = "empty"
        headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
        headers["cookie"] = "bev=1634362052_OWQ4MjQxMmU4YzU1; bm_sz=03806839A98795732D4AC3F951F959B1~YAAQ5wfSF2GgsFV8AQAAec+Rhw24j0zMgbviKV/YVmvXhj9tRKr7zsvlIIAfsiledM8UXS5kWPRdbs/EplpdHOYit4dLEZOAEj82HbKPatC65Pr0JeFPx4By0DBSjQ5PCWQnNs1uhTYM4TugKf1OtyhfdtdHa04+UWl8PMFDRKj2UOFb4IG/pqttWpzQUbm1BOOe2ET/0UdLnO8gt5dPYMKe2qzuBIMtFiq6bTFFGFz9oIvQmPlZn5bDP+VQr5QzuUitM8RN+3oX/Eso/JuMRIcEgZ8q8xgVNnCU0ctR1TJYomJD8OE=~3356740~3355703; _csrf_token=V4%24.airbnb.com.au%24hnpNs2fu9-E%24M7btLkHrQ0LvW_zbGGGFUMySzj0MeiFTi28beQam9Hc%3D; jitney_client_session_id=70c415c0-a45d-496b-9f9f-440ef03b13ed; jitney_client_session_created_at=1634362052; flags=0; _abck=BD7816B73F6D31BB3F978B5D4FEDF62F~0~YAAQ5wfSF2qgsFV8AQAA4tGRhwblxJr8qINR33zLB0nPotXGDDesvo2xkX+ZO9regFbX6g3ysHuSueYWZV8XgwjGhRs59iR5xHTFFPeDYJQ6wrX9AOSH02J5ZGPWXHBlui3tAJPEzleNJV04bpKWrsnHiwJMxfoU9airWKwcB8b1NseZThJFbBZ1wMQQuvRQ1akXjqqgEGcKtiWtFcyoWsxVRZqnw5wz3dZg0LrPGepqhJOgtZJCbXIAnISp48IdKa96YRokkiqL3oaKXUpI4uiaUBivHWlBx6yHy+wf/4l1nTYGDa+9TGgQJ076pmaml2nYq4ZImrskewb6T9YnMvQ2yDSoOclPoA6eRwkPzB11j721GzIKN2lP+G2dPbiQkGN/aQiKkEudM8kCKE0ESY703DZQOueSQ90=~-1~-1~-1; previousTab=%7B%22id%22%3A%22f6dbf0c9-7df6-4fd8-a720-ca2ca743ff33%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.com.au%2F%22%7D; jitney_client_session_updated_at=1634362053; frmfctr=wide; cfrmfctr=DESKTOP; _user_attributes=%7B%22guest_exchange%22%3A1.34785%2C%22device_profiling_session_id%22%3A%221634362052--2428bc162fa352668a6c7bab%22%2C%22giftcard_profiling_session_id%22%3A%221634362052--c67e3497b3197533c46c00bc%22%2C%22reservation_profiling_session_id%22%3A%221634362052--b1fe8214158589839aac980e%22%2C%22curr%22%3A%22AUD%22%7D"

        self.headers = headers
        self.session = requests.Session()
        self.session.headers.update(headers)

    def create_url(self,listing = "41088166"):
        base_url = "https://www.airbnb.com.au/api/v3/PdpAvailabilityCalendar?"
        variables = dict(request={"count": 12, "listingId": listing, "month": 10, "year": 2021})

        query = dict(operationName='PdpAvailabilityCalendar', locale='en-AU¤cy=AUD',
                         variables=json.dumps(variables),
                         extensions='{"persistedQuery":{"version":1,"sha256Hash":"8f08e03c7bd16fcad3c92a3592c19a8b559a0d0855a84028d1163d4733ed9ade"}}',
                         _cb='0lx0ysq1eadpy71g3vtdn0dmev91')

        params = parse.urlencode(query)
        self.url =  base_url + params

    def explore(self,location = "Glen Waverley"):
        resp = self.session.get(self.url)
        return resp.json()

airbnb = Airbnb()
airbnb.create_url()
airbnb.explore()

