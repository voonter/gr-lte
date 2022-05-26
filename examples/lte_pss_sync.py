# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: LTE PSS Sync
# Author: Johannes Demel
# Description: hierarchical blocks for PSS synchronization
# GNU Radio version: 3.10.1.1

from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from gnuradio import lte







class lte_pss_sync(gr.hier_block2):
    def __init__(self, fftlen=2048):
        gr.hier_block2.__init__(
            self, "LTE PSS Sync",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fftlen = fftlen

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 768e4
        self.freq = freq = 9326e5
        self.band = band = 5e6
        self.N_rb_dl_pss = N_rb_dl_pss = 6

        ##################################################
        # Blocks
        ##################################################
        self.sync_pss_tagger_cc_0 = lte.pss_tagger_cc(fftlen, "$id")
        self.sync_pss_symbol_selector_cvc_0 = lte.pss_symbol_selector_cvc(fftlen, "$id")
        self.sync_pss_lte_extract_subcarriers_vcvc_0 = lte.extract_subcarriers_vcvc(N_rb_dl_pss, fftlen, "$id")
        self.sync_pss_fft_vxx_0 = fft.fft_vcc(fftlen, True, window.rectangular(fftlen), False, 1)
        self.sync_pss_calculator_vcm_0 = lte.pss_calculator_vcm(fftlen, "$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.sync_pss_calculator_vcm_0, 'half_frame'), (self.sync_pss_symbol_selector_cvc_0, 'half_frame'))
        self.msg_connect((self.sync_pss_calculator_vcm_0, 'lock'), (self.sync_pss_symbol_selector_cvc_0, 'lock'))
        self.msg_connect((self.sync_pss_calculator_vcm_0, 'lock'), (self.sync_pss_tagger_cc_0, 'lock'))
        self.msg_connect((self.sync_pss_calculator_vcm_0, 'N_id_2'), (self.sync_pss_tagger_cc_0, 'N_id_2'))
        self.msg_connect((self.sync_pss_calculator_vcm_0, 'half_frame'), (self.sync_pss_tagger_cc_0, 'half_frame'))
        self.connect((self, 0), (self.sync_pss_symbol_selector_cvc_0, 0))
        self.connect((self, 0), (self.sync_pss_tagger_cc_0, 0))
        self.connect((self.sync_pss_fft_vxx_0, 0), (self.sync_pss_lte_extract_subcarriers_vcvc_0, 0))
        self.connect((self.sync_pss_lte_extract_subcarriers_vcvc_0, 0), (self.sync_pss_calculator_vcm_0, 0))
        self.connect((self.sync_pss_symbol_selector_cvc_0, 0), (self.sync_pss_fft_vxx_0, 0))
        self.connect((self.sync_pss_tagger_cc_0, 0), (self, 0))


    def get_fftlen(self):
        return self.fftlen

    def set_fftlen(self, fftlen):
        self.fftlen = fftlen

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_band(self):
        return self.band

    def set_band(self, band):
        self.band = band

    def get_N_rb_dl_pss(self):
        return self.N_rb_dl_pss

    def set_N_rb_dl_pss(self, N_rb_dl_pss):
        self.N_rb_dl_pss = N_rb_dl_pss

