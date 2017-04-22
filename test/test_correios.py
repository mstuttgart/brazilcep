# -*- coding: utf-8 -*-

import requests
from unittest import mock
from unittest import TestCase

from pycep_correios.correios import Correios
from pycep_correios.correios_exceptions import \
    CorreiosCEPInvalidCEPException
from pycep_correios.correios_exceptions import \
    CorreiosTimeOutException
from pycep_correios.correios_exceptions import \
    CorreiosCEPTooManyRedirectsException
from pycep_correios.correios_exceptions import \
    CorreiosCEPConnectionErrorException


class TestCorreios(TestCase):

    def setUp(self):
        self.response_xml = '''<S:Envelope xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
                                    <S:Body>
                                    <ns2:consultaCEPResponse
                                    xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
                                        <return>
                                            <bairro>Asa Norte</bairro>
                                            <cep>70002900</cep>
                                            <cidade>Brasília</cidade>
                                            <complemento/>
                                            <complemento2/>
                                            <end>SBN Quadra 1 Bloco A</end>
                                            <id>0</id>
                                            <uf>DF</uf>
                                        </return>
                                    </ns2:consultaCEPResponse>
                                    </S:Body>
                                    </S:Envelope>'''.replace('\n', '')

        self.response_xml_error = '''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body><soap:Fault>
                <faultcode>soap:Server</faultcode>
                <faultstring>BUSCA DEFINIDA COMO EXATA, 0 CEP DEVE TER 8 DIGITOS</faultstring>
                <detail><ns2:SigepClienteException xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/">
                BUSCA DEFINIDA COMO EXATA, 0 CEP DEVE TER 8 DIGITOS
                </ns2:SigepClienteException></detail></soap:Fault>
                </soap:Body></soap:Envelope>'''.replace('\n', '')

        self.expected_address = {
            'bairro': 'Asa Norte',
            'cidade': 'Brasília',
            'complemento': '',
            'outro': '',
            'rua': 'SBN Quadra 1 Bloco A',
            'uf': 'DF',
        }

    @mock.patch('pycep_correios.correios.requests.post')
    def test_get_cep(self, mock_api_call):

        mock_api_call.return_value = mock.MagicMock(status_code=200,
                                                    ok=True,
                                                    text=self.response_xml)

        self.assertDictEqual(Correios.get_cep('70002900'),
                             self.expected_address)

        mock_api_call.return_value = mock.MagicMock(ok=False,
                                                    text=self.response_xml_error)

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          Correios.get_cep, '1232710')

        mock_api_call.side_effect = requests.exceptions.Timeout()
        self.assertRaises(CorreiosTimeOutException,
                          Correios.get_cep, '12345-500')

        mock_api_call.side_effect = requests.exceptions.Timeout()
        self.assertRaises(CorreiosTimeOutException,
                          Correios.get_cep, '12345-500')

        mock_api_call.side_effect = requests.exceptions.TooManyRedirects()
        self.assertRaises(CorreiosCEPTooManyRedirectsException,
                          Correios.get_cep, '12345-500')

        mock_api_call.side_effect = requests.exceptions.ConnectionError()
        self.assertRaises(CorreiosCEPConnectionErrorException,
                          Correios.get_cep, '12345-500')

    def test__format_cep(self):
        self.assertRaises(CorreiosCEPInvalidCEPException,
                          Correios._format_cep, 37503003)

    def test__mount_request(self):

        HEADER = '<soap:Envelope ' \
             'xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" ' \
             'xmlns:cli=\"http://cliente.bean.master.sigep.bsb.correios.com' \
             '.br/\"><soap:Header/><soap:Body>'

        FOOTER = '</soap:Body></soap:Envelope>'

        cep='37503005'

        xml = HEADER
        xml += '<cli:consultaCEP>'
        xml += '<cep>%s</cep>' % cep
        xml += '</cli:consultaCEP>'
        xml += FOOTER

        self.assertEqual(xml, Correios._mount_request(cep=cep))

    def test__parse_response(self):

        response = Correios._parse_response(self.response_xml)
        self.assertDictEqual(response, self.expected_address)

    def test__parse_error(self):

        fault = Correios._parse_error(self.response_xml_error)
        self.assertEqual(fault, 'BUSCA DEFINIDA COMO EXATA, '
                                '0 CEP DEVE TER 8 DIGITOS')
