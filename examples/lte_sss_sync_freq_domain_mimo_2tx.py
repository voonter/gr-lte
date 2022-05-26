# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SSS Sync frequency Domain MIMO 2TX
# Author: Kristian Maier
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_sss_sync_freq_domain_mimo_2tx(gr.hier_block2):
    def __init__(self, N_rb_dl=50, rxant=2):
        gr.hier_block2.__init__(
            self, "SSS Sync frequency Domain MIMO 2TX",
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*N_rb_dl*12, gr.sizeof_gr_complex*N_rb_dl*12]),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*N_rb_dl*12, gr.sizeof_gr_complex*N_rb_dl*12]),
        )
        self.message_port_register_hier_in("N_id_2")
        self.message_port_register_hier_out("cell_id")

        ##################################################
        # Parameters
        ##################################################
        self.N_rb_dl = N_rb_dl
        self.rxant = rxant

        ##################################################
        # Blocks
        ##################################################
        self.lte_mimo_sss_tagger_0_0 = lte.mimo_sss_tagger(1, N_rb_dl)
        self.lte_mimo_sss_tagger_0 = lte.mimo_sss_tagger(1, N_rb_dl)
        self.lte_mimo_sss_symbol_selector_0_0_0 = lte.mimo_sss_symbol_selector(1, N_rb_dl)
        self.lte_mimo_sss_symbol_selector_0_0 = lte.mimo_sss_symbol_selector(1, N_rb_dl)
        self.lte_mimo_sss_calculator_0 = lte.mimo_sss_calculator(rxant)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*72, 2)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lte_mimo_sss_calculator_0, 'frame_start'), (self.lte_mimo_sss_tagger_0, 'frame_start'))
        self.msg_connect((self.lte_mimo_sss_calculator_0, 'frame_start'), (self.lte_mimo_sss_tagger_0_0, 'frame_start'))
        self.msg_connect((self.lte_mimo_sss_calculator_0, 'cell_id'), (self, 'cell_id'))
        self.msg_connect((self, 'N_id_2'), (self.lte_mimo_sss_calculator_0, 'N_id_2'))
        self.connect((self.blocks_streams_to_vector_0, 0), (self.lte_mimo_sss_calculator_0, 0))
        self.connect((self.lte_mimo_sss_symbol_selector_0_0, 0), (self.blocks_streams_to_vector_0, 0))
        self.connect((self.lte_mimo_sss_symbol_selector_0_0_0, 0), (self.blocks_streams_to_vector_0, 1))
        self.connect((self.lte_mimo_sss_tagger_0, 0), (self, 0))
        self.connect((self.lte_mimo_sss_tagger_0_0, 0), (self, 1))
        self.connect((self, 0), (self.lte_mimo_sss_symbol_selector_0_0, 0))
        self.connect((self, 1), (self.lte_mimo_sss_symbol_selector_0_0_0, 0))
        self.connect((self, 0), (self.lte_mimo_sss_tagger_0, 0))
        self.connect((self, 1), (self.lte_mimo_sss_tagger_0_0, 0))


    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl

    def get_rxant(self):
        return self.rxant

    def set_rxant(self, rxant):
        self.rxant = rxant

