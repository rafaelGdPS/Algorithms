from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message_valid = "trator"
    assert encrypt_message(message_valid, 4) == "ro_tart"
    assert encrypt_message(message_valid, 3) == "art_rot"
    assert encrypt_message(message_valid, 9) == "rotart"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message_valid, "5")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 4)
