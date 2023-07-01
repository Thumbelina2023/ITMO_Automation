def test_hw ():
    assert ('home','work') == ('home','work')

def test_qa_qc ():
    assert 'QA' != 'QC'

def test_not ():
    assert not (1,1,2,3,5) == (2,3,5)
