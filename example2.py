@htf.plug(source_meter=SourceMeterPlug, waveform_gen=WaveformGenPlug, multimeter=MultimeterPlug, dut=ZH521X)
@htf.PhaseOptions(timeout_s=300)


@htf.measures(htf.Measurement('highest_freq').with_units(htf.units.MEGAHERTZ)
              .with_dimensions(htf.Dimension(description='vdd', unit=htf.units.VOLT)).dimension_pivot_validate(validators.in_range(30, 50)))



def get_flash_highest_freq(test, mode, volt_list, waveform_channel, freq_start, freq_stop, freq_step, io_freq, source_meter:SourceMeterPlug, 
                           waveform_gen:WaveformGenPlug, multimeter:MultimeterPlug, dut:ZH521X):
    if not dut.set_mode(mode.value):
        return

    freq_list = get_flash_highest_reading_freq(test, waveform_gen, multimeter, dut, volt_list, waveform_channel, freq_start, freq_stop, 
                                               freq_step, io_freq)
    for elem in freq_list:
        volt, freq = elem
        test.measurements.highest_freq[volt] = freq/1000000
        output_measure_result(test, "mode %s: highest frequency of Flash at %fV is %fMHz", mode.name, volt, freq/1000000)
