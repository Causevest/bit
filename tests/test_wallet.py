import pytest

from bit.crypto import EllipticCurvePrivateKey
from bit.curve import Point
from bit.keygen import generate_private_key
from bit.wallet import Key, PrivateKey
from .samples import (
    BITCOIN_ADDRESS, BITCOIN_ADDRESS_TEST, PRIVATE_KEY_DER, PRIVATE_KEY_HEX,
    PRIVATE_KEY_PEM, PUBLIC_KEY_COMPRESSED, PUBLIC_KEY_UNCOMPRESSED,
    PUBLIC_KEY_X, PUBLIC_KEY_Y, WALLET_FORMAT_COMPRESSED_MAIN,
    WALLET_FORMAT_COMPRESSED_TEST, WALLET_FORMAT_MAIN, WALLET_FORMAT_TEST
)


class TestPrivateKey:
    def test_alias(self):
        assert Key == PrivateKey

    def test_init_default(self):
        private_key = PrivateKey()

        assert isinstance(private_key._pk, EllipticCurvePrivateKey)
        assert isinstance(private_key._public_point, Point)

        assert private_key._balance is None
        assert private_key._utxo == []
        assert private_key._transactions == []

        assert private_key._test_balance is None
        assert private_key._test_utxo == []
        assert private_key._test_transactions == []

    def test_init_from_key(self):
        pk = generate_private_key()
        private_key = PrivateKey(pk)
        assert private_key._pk == pk

    def test_init_from_wif(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.address == BITCOIN_ADDRESS

    def test_init_wif_error(self):
        with pytest.raises(ValueError):
            PrivateKey(b'\x00')

    def test_init_sync(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN, sync=True)
        assert len(private_key.transactions) > 0

    def test_address(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.address == BITCOIN_ADDRESS

    def test_test_address(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.test_address == BITCOIN_ADDRESS_TEST

    def test_public_key_compressed(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.public_key() == PUBLIC_KEY_COMPRESSED

    def test_public_key_uncompressed(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.public_key(compressed=False) == PUBLIC_KEY_UNCOMPRESSED

    def test_public_point(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.public_point == Point(PUBLIC_KEY_X, PUBLIC_KEY_Y)

    def test_to_wif(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.to_wif() == WALLET_FORMAT_MAIN
        assert private_key.to_wif(version='test') == WALLET_FORMAT_TEST
        assert private_key.to_wif(compressed=True) == WALLET_FORMAT_COMPRESSED_MAIN
        assert private_key.to_wif(version='test', compressed=True) == WALLET_FORMAT_COMPRESSED_TEST

    def test_to_hex(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.to_hex() == PRIVATE_KEY_HEX

    def test_to_der(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.to_der() == PRIVATE_KEY_DER

    def test_to_pem(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        assert private_key.to_pem() == PRIVATE_KEY_PEM

    def test_from_hex(self):
        assert PrivateKey.from_hex(PRIVATE_KEY_HEX).to_hex() == PRIVATE_KEY_HEX

    def test_from_der(self):
        assert PrivateKey.from_der(PRIVATE_KEY_DER).to_der() == PRIVATE_KEY_DER

    def test_from_pem(self):
        assert PrivateKey.from_pem(PRIVATE_KEY_PEM).to_pem() == PRIVATE_KEY_PEM

    def test_get_balance(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        balance = private_key.get_balance()
        assert balance == private_key.balance

    def test_get_utxo(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        utxo = private_key.get_utxo()
        assert utxo == private_key.utxo

    def test_get_transactions(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        transactions = private_key.get_transactions()
        assert transactions == private_key.transactions

    def test_sync(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        private_key.sync()
        assert len(private_key.transactions) > 0

    def test_get_test_balance(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        test_balance = private_key.get_test_balance()
        assert test_balance == private_key.test_balance

    def test_get_test_utxo(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        test_utxo = private_key.get_test_utxo()
        assert test_utxo == private_key.test_utxo

    def test_get_test_transactions(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        test_transactions = private_key.get_test_transactions()
        assert test_transactions == private_key.test_transactions

    def test_test_sync(self):
        private_key = PrivateKey(WALLET_FORMAT_MAIN)
        private_key.test_sync()
        assert len(private_key.test_transactions) > 0














