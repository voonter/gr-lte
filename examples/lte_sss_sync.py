# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: LTE SSS Sync
# Author: Johannes Demel
# Description: hierarchical block including blocks for LTE SSS synchronization.
# GNU Radio version: 3.10.1.1

from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from gnuradio import lte







class lte_sss_sync(gr.hier_block2):
    def __init__(self, N_rb_dl=50, fftlen=2048, group_key="N_id_2", offset_key="offset_marker"):
        gr.hier_block2.__init__(
            self, "LTE SSS Sync",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )
        self.message_port_register_hier_out("cell_id")

        ##################################################
        # Parameters
        ##################################################
        self.N_rb_dl = N_rb_dl
        self.fftlen = fftlen
        self.group_key = group_key
        self.offset_key = offset_key

        ##################################################
        # Blocks
        ##################################################
        self.sync_sss_tagger_cc_0 = lte.sss_tagger_cc(fftlen, "$id")
        self.sync_sss_symbol_selector_cvc_0 = lte.sss_symbol_selector_cvc(fftlen, "$id")
        self.sync_sss_fft_vxx_0 = fft.fft_vcc(fftlen, True, window.rectangular(fftlen), False, 1)
        self.sync_sss_extract_subcarriers_vcvc_0 = lte.extract_subcarriers_vcvc(6, fftlen, "$id")
        self.sync_sss_calculator_vcm_0 = lte.sss_calculator_vcm(fftlen, group_key, offset_key, "$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.sync_sss_calculator_vcm_0, 'cell_id'), (self, 'cell_id'))
        self.msg_connect((self.sync_sss_calculator_vcm_0, 'frame_start'), (self.sync_sss_tagger_cc_0, 'frame_start'))
        self.connect((self, 0), (self.sync_sss_symbol_selector_cvc_0, 0))
        self.connect((self, 0), (self.sync_sss_tagger_cc_0, 0))
        self.connect((self.sync_sss_extract_subcarriers_vcvc_0, 0), (self.sync_sss_calculator_vcm_0, 0))
        self.connect((self.sync_sss_fft_vxx_0, 0), (self.sync_sss_extract_subcarriers_vcvc_0, 0))
        self.connect((self.sync_sss_symbol_selector_cvc_0, 0), (self.sync_sss_fft_vxx_0, 0))
        self.connect((self.sync_sss_tagger_cc_0, 0), (self, 0))


    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl

    def get_fftlen(self):
        return self.fftlen

    def set_fftlen(self, fftlen):
        self.fftlen = fftlen

    def get_group_key(self):
        return self.group_key

    def set_group_key(self, group_key):
        self.group_key = group_key

    def get_offset_key(self):
        return self.offset_key

    def set_offset_key(self, offset_key):
        self.offset_key = offset_key

