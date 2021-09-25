# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


class ValidateSearchForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_search_form"

    @classmethod
    def item_db(cls) -> List[Text]:
        return [
            "消费记录",
            "套餐类型",
            "剩余流量",
            "话费余额"
        ]

    @classmethod
    def time_db(cls) -> List[Text]:
        return [
            "一月",
            "二月",
            "三月",
            "四月",
            "五月",
            "六月",
            "七月",
            "八月",
            "九月",
            "十月",
            "十一月",
            "十二月",
            "本月",
            "上月"
        ]

    def validate_time(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value in self.time_db():
            return {"time": value}
        else:
            dispatcher.utter_message(response="utter_wrong_time")
            return {"time": None}

    def validate_item(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value in self.item_db():
            return {"item": value}
        else:
            dispatcher.utter_message(response="utter_wrong_item")
            return {"item": None}

