# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PCFICH Decoder
# Author: Johannes Demel
# Description: hier block combining blocks and parameters to decode PCFICH
# GNU Radio version: 3.10.1.1

from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_pcfich_decoder(gr.hier_block2):
    def __init__(self, N_rb_dl=50, key="symbol"):
        gr.hier_block2.__init__(
            self, "PCFICH Decoder",
                gr.io_signature.makev(3, 3, [gr.sizeof_gr_complex*12 * N_rb_dl, gr.sizeof_gr_complex*12 * N_rb_dl, gr.sizeof_gr_complex*12 * N_rb_dl]),
                gr.io_signature(0, 0, 0),
        )
        self.message_port_register_hier_in("N_ant")
        self.message_port_register_hier_in("cell_id")
        self.message_port_register_hier_out("CFI")

        ##################################################
        # Parameters
        ##################################################
        self.N_rb_dl = N_rb_dl
        self.key = key

        ##################################################
        # Variables
        ##################################################
        self.vlen = vlen = 16
        self.tag_key = tag_key = "subframe"
        self.style = style = "tx_diversity"
        self.ants = ants = 2

        ##################################################
        # Blocks
        ##################################################
        self.pcfich_unpack_vfm_0 = lte.pcfich_unpack_vfm(tag_key, "CFI", "$id")
        self.pcfich_scramble_sequencer_m_0 = lte.pcfich_scramble_sequencer_m("$id")
        self.pcfich_qpsk_soft_demod_vcvf_0 = lte.qpsk_soft_demod_vcvf(vlen, "$id")
        self.pcfich_pre_decoder_vcvc_0 = lte.pre_decoder_vcvc(1, ants, vlen, style)
        self.pcfich_lte_descrambler_vfvf_0 = lte.descrambler_vfvf(tag_key, "seqs", 2 * vlen, "$id")
        self.pcfich_lte_descrambler_vfvf_0.set_descr_seqs([[0] * 32] * 10)
        self.pcfich_layer_demapper_vcvc_0 = lte.layer_demapper_vcvc(ants, vlen, style, "$id")
        self.pcfich_demux_vcvc_2 = lte.pcfich_demux_vcvc(N_rb_dl, key, tag_key, "cell_id", "$id")
        self.pcfich_demux_vcvc_1 = lte.pcfich_demux_vcvc(N_rb_dl, key, tag_key, "cell_id", "$id")
        self.pcfich_demux_vcvc_0 = lte.pcfich_demux_vcvc(N_rb_dl, key, tag_key, "cell_id", "$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.pcfich_scramble_sequencer_m_0, 'descr'), (self.pcfich_lte_descrambler_vfvf_0, 'seqs'))
        self.msg_connect((self.pcfich_unpack_vfm_0, 'CFI'), (self, 'CFI'))
        self.msg_connect((self, 'N_ant'), (self.pcfich_layer_demapper_vcvc_0, 'N_ant'))
        self.msg_connect((self, 'N_ant'), (self.pcfich_pre_decoder_vcvc_0, 'N_ant'))
        self.msg_connect((self, 'cell_id'), (self.pcfich_scramble_sequencer_m_0, 'cell_id'))
        self.connect((self, 0), (self.pcfich_demux_vcvc_0, 0))
        self.connect((self, 1), (self.pcfich_demux_vcvc_1, 0))
        self.connect((self, 2), (self.pcfich_demux_vcvc_2, 0))
        self.connect((self.pcfich_demux_vcvc_0, 0), (self.pcfich_pre_decoder_vcvc_0, 0))
        self.connect((self.pcfich_demux_vcvc_1, 0), (self.pcfich_pre_decoder_vcvc_0, 1))
        self.connect((self.pcfich_demux_vcvc_2, 0), (self.pcfich_pre_decoder_vcvc_0, 2))
        self.connect((self.pcfich_layer_demapper_vcvc_0, 0), (self.pcfich_qpsk_soft_demod_vcvf_0, 0))
        self.connect((self.pcfich_lte_descrambler_vfvf_0, 0), (self.pcfich_unpack_vfm_0, 0))
        self.connect((self.pcfich_pre_decoder_vcvc_0, 0), (self.pcfich_layer_demapper_vcvc_0, 0))
        self.connect((self.pcfich_qpsk_soft_demod_vcvf_0, 0), (self.pcfich_lte_descrambler_vfvf_0, 0))


    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_vlen(self):
        return self.vlen

    def set_vlen(self, vlen):
        self.vlen = vlen

    def get_tag_key(self):
        return self.tag_key

    def set_tag_key(self, tag_key):
        self.tag_key = tag_key

    def get_style(self):
        return self.style

    def set_style(self, style):
        self.style = style

    def get_ants(self):
        return self.ants

    def set_ants(self, ants):
        self.ants = ants

