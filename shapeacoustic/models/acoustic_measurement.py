def AcousticMeasurement(beamforming, source, receiver, **kwargs):
    """
    Acoustic measurement model.

    Parameters
    ----------
    beamforming : Beamforming
        Beamforming model.
    source : Source
        Source model.
    receiver : Receiver
        Receiver model.

    Returns
    -------
    acoustic_measurement : ndarray
        Acoustic measurement.
    """
    # Acoustic measurement
    acoustic_measurement = beamforming(source, receiver, **kwargs)

    return acoustic_measurement