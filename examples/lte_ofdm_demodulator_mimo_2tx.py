# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: OFDM Demodulator MIMO 2TX
# Author: Johannes Demel, Kristian Maier
# GNU Radio version: 3.10.1.1

from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from gnuradio import lte







class lte_ofdm_demodulator_mimo_2tx(gr.hier_block2):
    def __init__(self, N_rb_dl=50, fftlen=1024, ofdm_key="slot", rxant=2):
        gr.hier_block2.__init__(
            self, "OFDM Demodulator MIMO 2TX",
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*12*N_rb_dl, gr.sizeof_gr_complex*12*N_rb_dl]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.N_rb_dl = N_rb_dl
        self.fftlen = fftlen
        self.ofdm_key = ofdm_key
        self.rxant = rxant

        ##################################################
        # Blocks
        ##################################################
        self.ofdm_fft_vxx_0_0 = fft.fft_vcc(fftlen, True, window.rectangular(fftlen), False, 1)
        self.ofdm_fft_vxx_0 = fft.fft_vcc(fftlen, True, window.rectangular(fftlen), False, 1)
        self.lte_mimo_remove_cp_0 = lte.mimo_remove_cp(fftlen, rxant, ofdm_key)
        self.lte_extract_subcarriers_vcvc_0_0 = lte.extract_subcarriers_vcvc(N_rb_dl, fftlen, "$id")
        self.lte_extract_subcarriers_vcvc_0 = lte.extract_subcarriers_vcvc(N_rb_dl, fftlen, "$id")


        ##################################################
        # Connections
        ##################################################
        self.connect((self.lte_extract_subcarriers_vcvc_0, 0), (self, 0))
        self.connect((self.lte_extract_subcarriers_vcvc_0_0, 0), (self, 1))
        self.connect((self.lte_mimo_remove_cp_0, 0), (self.ofdm_fft_vxx_0, 0))
        self.connect((self.lte_mimo_remove_cp_0, 1), (self.ofdm_fft_vxx_0_0, 0))
        self.connect((self.ofdm_fft_vxx_0, 0), (self.lte_extract_subcarriers_vcvc_0, 0))
        self.connect((self.ofdm_fft_vxx_0_0, 0), (self.lte_extract_subcarriers_vcvc_0_0, 0))
        self.connect((self, 0), (self.lte_mimo_remove_cp_0, 0))
        self.connect((self, 1), (self.lte_mimo_remove_cp_0, 1))


    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl

    def get_fftlen(self):
        return self.fftlen

    def set_fftlen(self, fftlen):
        self.fftlen = fftlen

    def get_ofdm_key(self):
        return self.ofdm_key

    def set_ofdm_key(self, ofdm_key):
        self.ofdm_key = ofdm_key

    def get_rxant(self):
        return self.rxant

    def set_rxant(self, rxant):
        self.rxant = rxant

