from pytest_bdd import scenario, given, when, then, parsers

@scenario("open_date.feature", "Opening an empty slot before its respective date")
def test_empty_slot_before_date():
    pass

@given(parsers.parse("I have a slot without text or an image for date {date:String}"))
def i_have_empty_slot_for_date(date: str):
    pass

