# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PBCH Decoder
# Author: Johannes Demel
# Description: hierarchical block to decode PBCH
# GNU Radio version: 3.10.1.1

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
from gnuradio import lte
from lte_pbch_descrambler import lte_pbch_descrambler  # grc-generated hier_block







class lte_pbch_decoder(gr.hier_block2):
    def __init__(self, N_rb_dl=50):
        gr.hier_block2.__init__(
            self, "PBCH Decoder",
                gr.io_signature.makev(3, 3, [gr.sizeof_gr_complex*12*N_rb_dl, gr.sizeof_gr_complex*12*N_rb_dl, gr.sizeof_gr_complex*12*N_rb_dl]),
                gr.io_signature(1, 1, gr.sizeof_float*120),
        )
        self.message_port_register_hier_in("cell_id")

        ##################################################
        # Parameters
        ##################################################
        self.N_rb_dl = N_rb_dl

        ##################################################
        # Variables
        ##################################################
        self.vlen = vlen = 240
        self.style = style = "tx_diversity"
        self.pbch_descr_key = pbch_descr_key = "descr_part"

        ##################################################
        # Blocks
        ##################################################
        self.pbch_qpsk_soft_demod_vcvf_0 = lte.qpsk_soft_demod_vcvf(vlen, "$id")
        self.pbch_layer_demapper_vcvc_1 = lte.layer_demapper_vcvc(2, vlen, style, "$id")
        self.pbch_layer_demapper_vcvc_0 = lte.layer_demapper_vcvc(1, vlen, style, "$id")
        self.pbch_blocks_interleave_0 = blocks.interleave(gr.sizeof_gr_complex*vlen, 1)
        self.lte_pre_decoder_vcvc_1 = lte.pre_decoder_vcvc(1, 2, vlen, style)
        self.lte_pre_decoder_vcvc_0 = lte.pre_decoder_vcvc(1, 1, vlen, style)
        self.lte_pbch_descrambler_0 = lte_pbch_descrambler()
        self.lte_pbch_demux_vcvc_0_1 = lte.pbch_demux_vcvc(N_rb_dl, 1, "$id")
        self.lte_pbch_demux_vcvc_0_0 = lte.pbch_demux_vcvc(N_rb_dl, 1, "$id")
        self.lte_pbch_demux_vcvc_0 = lte.pbch_demux_vcvc(N_rb_dl, 1, "$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self, 'cell_id'), (self.lte_pbch_demux_vcvc_0, 'cell_id'))
        self.msg_connect((self, 'cell_id'), (self.lte_pbch_demux_vcvc_0_0, 'cell_id'))
        self.msg_connect((self, 'cell_id'), (self.lte_pbch_demux_vcvc_0_1, 'cell_id'))
        self.msg_connect((self, 'cell_id'), (self.lte_pbch_descrambler_0, 'cell_id'))
        self.connect((self.lte_pbch_demux_vcvc_0, 0), (self.lte_pre_decoder_vcvc_0, 0))
        self.connect((self.lte_pbch_demux_vcvc_0, 0), (self.lte_pre_decoder_vcvc_1, 0))
        self.connect((self.lte_pbch_demux_vcvc_0_0, 0), (self.lte_pre_decoder_vcvc_1, 2))
        self.connect((self.lte_pbch_demux_vcvc_0_1, 0), (self.lte_pre_decoder_vcvc_0, 1))
        self.connect((self.lte_pbch_demux_vcvc_0_1, 0), (self.lte_pre_decoder_vcvc_1, 1))
        self.connect((self.lte_pbch_descrambler_0, 0), (self, 0))
        self.connect((self.lte_pre_decoder_vcvc_0, 0), (self.pbch_layer_demapper_vcvc_0, 0))
        self.connect((self.lte_pre_decoder_vcvc_1, 0), (self.pbch_layer_demapper_vcvc_1, 0))
        self.connect((self, 0), (self.lte_pbch_demux_vcvc_0, 0))
        self.connect((self, 1), (self.lte_pbch_demux_vcvc_0_1, 0))
        self.connect((self, 2), (self.lte_pbch_demux_vcvc_0_0, 0))
        self.connect((self.pbch_blocks_interleave_0, 0), (self.pbch_qpsk_soft_demod_vcvf_0, 0))
        self.connect((self.pbch_layer_demapper_vcvc_0, 0), (self.pbch_blocks_interleave_0, 0))
        self.connect((self.pbch_layer_demapper_vcvc_1, 0), (self.pbch_blocks_interleave_0, 1))
        self.connect((self.pbch_qpsk_soft_demod_vcvf_0, 0), (self.lte_pbch_descrambler_0, 0))


    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl

    def get_vlen(self):
        return self.vlen

    def set_vlen(self, vlen):
        self.vlen = vlen

    def get_style(self):
        return self.style

    def set_style(self, style):
        self.style = style

    def get_pbch_descr_key(self):
        return self.pbch_descr_key

    def set_pbch_descr_key(self, pbch_descr_key):
        self.pbch_descr_key = pbch_descr_key

