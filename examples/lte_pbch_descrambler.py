# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PBCH Descrambler
# Author: Johannes Demel
# Description: Block to descramble PBCH
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_pbch_descrambler(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "PBCH Descrambler",
                gr.io_signature(1, 1, gr.sizeof_float*480),
                gr.io_signature(1, 1, gr.sizeof_float*120),
        )
        self.message_port_register_hier_in("cell_id")

        ##################################################
        # Blocks
        ##################################################
        self.pbch_descr_scramble_sequencer_m_0 = lte.pbch_scramble_sequencer_m("$id")
        self.pbch_descr_repeat_message_source_vf_0 = lte.repeat_message_source_vf(1920, "$id")
        self.pbch_descr_blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*120, 16)
        self.pbch_descr_blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*480, 4)
        self.pbch_descr_blocks_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_float*120, 4)
        self.pbch_descr_blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_float*120, 4, 1)
        self.pbch_descr_blocks_repeat_0 = blocks.repeat(gr.sizeof_float*480, 4)
        self.pbch_descr_blocks_multiply_xx_0 = blocks.multiply_vff(1920)
        self.pbch_descr_blocks_multiply_const_vxx_0 = blocks.multiply_const_vff([1/4.0]*120)
        self.pbch_descr_blocks_add_xx_0 = blocks.add_vff(120)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self, 'cell_id'), (self.pbch_descr_scramble_sequencer_m_0, 'cell_id'))
        self.msg_connect((self.pbch_descr_scramble_sequencer_m_0, 'vector'), (self.pbch_descr_repeat_message_source_vf_0, 'vector'))
        self.connect((self, 0), (self.pbch_descr_blocks_repeat_0, 0))
        self.connect((self.pbch_descr_blocks_add_xx_0, 0), (self.pbch_descr_blocks_multiply_const_vxx_0, 0))
        self.connect((self.pbch_descr_blocks_multiply_const_vxx_0, 0), (self.pbch_descr_blocks_stream_mux_0, 1))
        self.connect((self.pbch_descr_blocks_multiply_xx_0, 0), (self.pbch_descr_blocks_vector_to_stream_0, 0))
        self.connect((self.pbch_descr_blocks_repeat_0, 0), (self.pbch_descr_blocks_stream_to_vector_0, 0))
        self.connect((self.pbch_descr_blocks_stream_mux_0, 0), (self, 0))
        self.connect((self.pbch_descr_blocks_stream_to_streams_0, 1), (self.pbch_descr_blocks_add_xx_0, 1))
        self.connect((self.pbch_descr_blocks_stream_to_streams_0, 2), (self.pbch_descr_blocks_add_xx_0, 2))
        self.connect((self.pbch_descr_blocks_stream_to_streams_0, 3), (self.pbch_descr_blocks_add_xx_0, 3))
        self.connect((self.pbch_descr_blocks_stream_to_streams_0, 0), (self.pbch_descr_blocks_add_xx_0, 0))
        self.connect((self.pbch_descr_blocks_stream_to_vector_0, 0), (self.pbch_descr_blocks_multiply_xx_0, 0))
        self.connect((self.pbch_descr_blocks_vector_to_stream_0, 0), (self.pbch_descr_blocks_stream_mux_0, 0))
        self.connect((self.pbch_descr_blocks_vector_to_stream_0, 0), (self.pbch_descr_blocks_stream_to_streams_0, 0))
        self.connect((self.pbch_descr_repeat_message_source_vf_0, 0), (self.pbch_descr_blocks_multiply_xx_0, 1))


