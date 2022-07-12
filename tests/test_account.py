from scripts.helpful_scripts import get_account


def test_account():
    account = get_account()
    assert account.address == "0x2e25B53AFe79E69eAE06FB8D1433144f1D869c88"
