# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: LTE OFDM Demodulator
# Author: Johannes Demel
# Description: OFDM RX operations
# GNU Radio version: 3.10.1.1

from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from gnuradio import lte







class lte_ofdm_demodulator(gr.hier_block2):
    def __init__(self, N_rb_dl=50, fftlen=2048, ofdm_key="slot"):
        gr.hier_block2.__init__(
            self, "LTE OFDM Demodulator",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*12*N_rb_dl),
        )

        ##################################################
        # Parameters
        ##################################################
        self.N_rb_dl = N_rb_dl
        self.fftlen = fftlen
        self.ofdm_key = ofdm_key

        ##################################################
        # Blocks
        ##################################################
        self.ofdm_lte_remove_cp_cvc_0 = lte.remove_cp_cvc(fftlen, ofdm_key, "$id")
        self.ofdm_lte_extract_subcarriers_vcvc_0 = lte.extract_subcarriers_vcvc(N_rb_dl, fftlen, "$id")
        self.ofdm_fft_vxx_0 = fft.fft_vcc(fftlen, True, window.rectangular(fftlen), False, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ofdm_fft_vxx_0, 0), (self.ofdm_lte_extract_subcarriers_vcvc_0, 0))
        self.connect((self.ofdm_lte_extract_subcarriers_vcvc_0, 0), (self, 0))
        self.connect((self.ofdm_lte_remove_cp_cvc_0, 0), (self.ofdm_fft_vxx_0, 0))
        self.connect((self, 0), (self.ofdm_lte_remove_cp_cvc_0, 0))


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

