#
# This file contains the Top PAG reference selection work-flow for mu + jets analysis.
# as defined in
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopLeptonPlusJetsRefSel_mu#Selection_Version_SelV4_valid_fr
#

import sys

import FWCore.ParameterSet.Config as cms

process = cms.Process( 'PAT' )


### ======================================================================== ###
###                                                                          ###
###                                 Constants                                ###
###                            (user job steering)                           ###
###                                                                          ###
### ======================================================================== ###


### Data or MC?
runOnMC = True

### Standard and PF work flow

# Standard
runStandardPAT = True
usePFJets      = True
useCaloJets    = True

# PF2PAT
runPF2PAT = True

### Switch on/off selection steps

# Step 0a
useTrigger      = True
# Step 0b
useGoodVertex   = True
# Step 1a
useLooseMuon    = True
# Step 1b
useTightMuon    = True
# Step 2
useMuonVeto     = True
# Step 3
useElectronVeto = True
# Step 4a
use1Jet         = True
# Step 4b
use2Jets        = False
# Step 4c
use3Jets        = False
# Step 5
use4Jets        = False
# Step 6
useBTag         = False

addTriggerMatching = True

### Reference selection

from TopQuarkAnalysis.Configuration.patRefSel_refMuJets import *
# Muons general
#muonsUsePV             = False
#muonEmbedTrack         = True
#muonJetsDR             = 0.3
# Standard mouns
#muonCut                = ''
#looseMuonCut           = ''
#tightMuonCut           = ''
# PF muons
#muonCutPF              = ''
#looseMuonCutPF         = ''
#tightMuonCutPF         = ''
# Standard electrons
#electronCut            = ''
# PF electrons
#electronCutPF          = ''
# Calo jets
#jetCut                 = ''
# PF jets
#jetCutPF               = ''
#jetMuonsDRPF           = 0.1

# Trigger selection according to run range resp. MC sample:
# lower range limits for data available as suffix;
# available are: 000000, 147196, 160404, 163270, 173236, 175832 (default)
# sample name for MC available as suffix;
# available are: Summer11, Fall11 (default)
#triggerSelectionData       = triggerSelection_175832
#triggerObjectSelectionData = triggerObjectSelection_175832
#triggerSelectionMC       = triggerSelection_Fall11
#triggerObjectSelectionMC = triggerObjectSelection_Fall11

### Particle flow
### takes effect only, if 'runPF2PAT' = True

postfix = 'PF' # needs to be a non-empty string, if 'runStandardPAT' = True

# subtract charged hadronic pile-up particles (from wrong PVs)
# effects also JECs
usePFnoPU       = True  # before any top projection
usePfIsoLessCHS = False # switch to new PF isolation with L1Fastjet CHS

# other switches for PF top projections (default: all 'True')
useNoMuon     = True # before electron top projection
useNoElectron = True # before jet top projection
useNoJet      = True # before tau top projection
useNoTau      = True # before MET top projection

# cuts used in top projections
# vertices
#pfVertices  = 'goodOfflinePrimaryVertices'
#pfD0Cut     = 0.2
#pfDzCut     = 0.5
# muons
#pfMuonSelectionCut = 'pt > 5.'
useMuonCutBasePF = False # use minimal (veto) muon selection cut on top of 'pfMuonSelectionCut'
#pfMuonIsoConeR03 = False
#pfMuonCombIsoCut = 0.2
# electrons
#pfElectronSelectionCut  = 'pt > 5. && gsfTrackRef.isNonnull && gsfTrackRef.trackerExpectedHitsInner.numberOfLostHits < 2'
useElectronCutBasePF  = False # use minimal (veto) electron selection cut on top of 'pfElectronSelectionCut'
#pfElectronnIsoConeR03 = False
#pfElectronCombIsoCut  = 0.2

### JEC levels

# levels to be accessible from the jets
# jets are corrected to L3Absolute (MC), L2L3Residual (data) automatically, if enabled here
# and remain uncorrected, if none of these levels is enabled here
useL1FastJet    = True  # needs useL1Offset being off, error otherwise
useL1Offset     = False # needs useL1FastJet being off, error otherwise
useL2Relative   = True
useL3Absolute   = True
useL2L3Residual = True  # takes effect only on data
useL5Flavor     = False
useL7Parton     = False

### Input

# list of input files
useRelVals = True # if 'False', "inputFiles" is used
inputFiles = [ '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/179/411/E6068DCF-61FE-E011-B2C4-0019B9F72CE5.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/04C16888-52FB-E011-8321-0030486730C6.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/06B5F82F-57FB-E011-93CD-001D09F23A84.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/14675371-FBFA-E011-92EE-00215AEDFCCC.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/160F73C0-BAFA-E011-ADD0-001D09F2A465.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/2C9D2B89-B3FA-E011-AF19-001D09F24303.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/3A176EDF-BFFA-E011-90EA-003048CFB40C.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/4A2BDEC2-51FB-E011-9A27-BCAEC532971A.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/4AA63498-50FB-E011-A4E4-0025B32035BC.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/66B2E464-C0FA-E011-AFD8-BCAEC5329702.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/6C4DF9D2-BFFA-E011-BDCC-0019B9F709A4.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/6E3F588A-C4FA-E011-A20F-001D09F2527B.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/ACD7155F-B6FA-E011-95A9-BCAEC5329726.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/AEB720EB-46FB-E011-A1BE-003048F117F6.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/B4353A8A-C4FA-E011-BE51-0019B9F709A4.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/CCE2406E-FBFA-E011-9BCB-BCAEC53296FC.root'
             , '/store/data/Run2011B/MuHad/AOD/PromptReco-v1/000/178/866/D8F22FD9-B2FA-E011-8D39-BCAEC518FF8A.root '
             ] # overwritten, if "useRelVals" is 'True'

# maximum number of events
maxInputEvents = -1 # reduce for testing

### Conditions

# GlobalTags (w/o suffix '::All')
globalTagData = 'GR_R_42_V23'
globalTagMC   = 'START42_V17'

### Output

# output file
outputFile = 'patRefSel_muJets.root'

# event frequency of Fwk report
fwkReportEvery = 1000

# switch for 'TrigReport'/'TimeReport' at job end
wantSummary = True


###                              End of constants                            ###
###                                                                          ###
### ======================================================================== ###


###
### Basic configuration
###

process.load( "TopQuarkAnalysis.Configuration.patRefSel_basics_cff" )
process.MessageLogger.cerr.FwkReport.reportEvery = fwkReportEvery
process.options.wantSummary = wantSummary
if runOnMC:
  process.GlobalTag.globaltag = globalTagMC   + '::All'
else:
  process.GlobalTag.globaltag = globalTagData + '::All'


###
### Input configuration
###

process.load( "TopQuarkAnalysis.Configuration.patRefSel_inputModule_cfi" )
if useRelVals:
  from PhysicsTools.PatAlgos.tools.cmsswVersionTools import pickRelValInputFiles
  if runOnMC:
    inputFiles = pickRelValInputFiles( cmsswVersion  = 'CMSSW_4_2_6'
                                     , globalTag     = 'START42_V12'
                                     , maxVersions   = 1
                                     )
  else:
    inputFiles = pickRelValInputFiles( cmsswVersion  = 'CMSSW_4_2_6'
                                     , dataTier      = 'RECO'
                                     , relVal        = 'Mu'
                                     , globalTag     = 'GR_R_42_V14_wzMu2010B'
                                     , maxVersions   = 1
                                     )
process.source.fileNames = inputFiles
process.maxEvents.input  = maxInputEvents


###
### Output configuration
###

process.load( "TopQuarkAnalysis.Configuration.patRefSel_outputModule_cff" )
# output file name
process.out.fileName = outputFile
# event content
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out.outputCommands += patEventContent
# clear event selection
process.out.SelectEvents.SelectEvents = []


###
### Cleaning and trigger selection configuration
###

### Trigger selection
if runOnMC:
  triggerSelection = triggerSelectionMC
else:
  triggerSelection = triggerSelectionData
from TopQuarkAnalysis.Configuration.patRefSel_triggerSelection_cff import triggerResults
process.step0a = triggerResults.clone(
  triggerConditions = [ triggerSelection ]
)

### Good vertex selection
process.load( "TopQuarkAnalysis.Configuration.patRefSel_goodVertex_cfi" )
process.step0b = process.goodOfflinePrimaryVertices.clone( filter = True )

### Event cleaning
process.load( 'TopQuarkAnalysis.Configuration.patRefSel_eventCleaning_cff' )
process.step0c = cms.Sequence(
  process.HBHENoiseFilter
+ process.scrapingFilter
)


###
### PAT/PF2PAT configuration
###

pfSuffix = 'PF'
if runStandardPAT and runPF2PAT:
  if postfix == '':
    sys.exit( 'ERROR: running standard PAT and PF2PAT in parallel requires a defined "postfix" for PF2PAT' )
  if usePFJets:
    if postfix == 'Add' + pfSuffix or postfix == jetAlgo + pfSuffix:
      sys.exit( 'ERROR: running standard PAT with additional PF jets  and PF2PAT in parallel does not allow for the "postfix" %s'%( postfix ) )
if not runStandardPAT and not runPF2PAT:
  sys.exit( 'ERROR: standard PAT and PF2PAT are both switched off' )

process.load( "PhysicsTools.PatAlgos.patSequences_cff" )
from PhysicsTools.PatAlgos.tools.coreTools import *

### Check JECs

# JEC set
jecSet      = jecSetBase + 'Calo'
jecSetAddPF = jecSetBase + pfSuffix
jecSetPF    = jecSetAddPF
if usePFnoPU:
  jecSetPF += 'chs'

# JEC levels
if useL1FastJet and useL1Offset:
  sys.exit( 'ERROR: switch off either "L1FastJet" or "L1Offset"' )
jecLevels = []
if useL1FastJet:
  jecLevels.append( 'L1FastJet' )
if useL1Offset:
  jecLevels.append( 'L1Offset' )
if useL2Relative:
  jecLevels.append( 'L2Relative' )
if useL3Absolute:
  jecLevels.append( 'L3Absolute' )
if useL2L3Residual and not runOnMC:
  jecLevels.append( 'L2L3Residual' )
if useL5Flavor:
  jecLevels.append( 'L5Flavor' )
if useL7Parton:
  jecLevels.append( 'L7Parton' )

### Switch configuration

if runPF2PAT:
  if useMuonCutBasePF:
    pfMuonSelectionCut += ' && %s'%( muonCutBase )
  if useElectronCutBasePF:
    pfElectronSelectionCut += ' && %s'%( electronCutBase )
  from PhysicsTools.PatAlgos.tools.pfTools import usePF2PAT
  usePF2PAT( process
           , runPF2PAT      = runPF2PAT
           , runOnMC        = runOnMC
           , jetAlgo        = jetAlgo
           , postfix        = postfix
           , jetCorrections = ( jecSetPF
                              , jecLevels
                              )
           )
  applyPostfix( process, 'pfNoPileUp'  , postfix ).enable = usePFnoPU
  applyPostfix( process, 'pfNoMuon'    , postfix ).enable = useNoMuon
  applyPostfix( process, 'pfNoElectron', postfix ).enable = useNoElectron
  applyPostfix( process, 'pfNoJet'     , postfix ).enable = useNoJet
  applyPostfix( process, 'pfNoTau'     , postfix ).enable = useNoTau
  applyPostfix( process, 'pfPileUp', postfix ).Vertices = cms.InputTag( pfVertices )
  if useL1FastJet:
    applyPostfix( process, 'pfPileUp'   , postfix ).checkClosestZVertex = False
    applyPostfix( process, 'pfPileUpIso', postfix ).checkClosestZVertex = usePfIsoLessCHS
    applyPostfix( process, 'pfJets', postfix ).doAreaFastjet = True
    applyPostfix( process, 'pfJets', postfix ).doRhoFastjet  = False
  applyPostfix( process, 'pfMuonsFromVertex'    , postfix ).vertices = cms.InputTag( pfVertices )
  applyPostfix( process, 'pfMuonsFromVertex'    , postfix ).d0Cut    = pfD0Cut
  applyPostfix( process, 'pfMuonsFromVertex'    , postfix ).dzCut    = pfDzCut
  applyPostfix( process, 'pfSelectedMuons'      , postfix ).cut = pfMuonSelectionCut
  applyPostfix( process, 'pfIsolatedMuons'      , postfix ).isolationCut = pfMuonCombIsoCut
  if pfMuonIsoConeR03:
    applyPostfix( process, 'pfIsolatedMuons', postfix ).isolationValueMapsCharged  = cms.VInputTag( cms.InputTag( 'muPFIsoValueCharged03' + postfix )
                                                                                                  )
    applyPostfix( process, 'pfIsolatedMuons', postfix ).deltaBetaIsolationValueMap = cms.InputTag( 'muPFIsoValuePU03' + postfix )
    applyPostfix( process, 'pfIsolatedMuons', postfix ).isolationValueMapsNeutral  = cms.VInputTag( cms.InputTag( 'muPFIsoValueNeutral03' + postfix )
                                                                                                  , cms.InputTag( 'muPFIsoValueGamma03' + postfix )
                                                                                                  )
    applyPostfix( process, 'pfMuons', postfix ).isolationValueMapsCharged  = cms.VInputTag( cms.InputTag( 'muPFIsoValueCharged03' + postfix )
                                                                                          )
    applyPostfix( process, 'pfMuons', postfix ).deltaBetaIsolationValueMap = cms.InputTag( 'muPFIsoValuePU03' + postfix )
    applyPostfix( process, 'pfMuons', postfix ).isolationValueMapsNeutral  = cms.VInputTag( cms.InputTag( 'muPFIsoValueNeutral03' + postfix )
                                                                                          , cms.InputTag( 'muPFIsoValueGamma03' + postfix )
                                                                                          )
    applyPostfix( process, 'patMuons', postfix ).isolationValues.pfNeutralHadrons   = cms.InputTag( 'muPFIsoValueNeutral03' + postfix )
    applyPostfix( process, 'patMuons', postfix ).isolationValues.pfChargedAll       = cms.InputTag( 'muPFIsoValueChargedAll03' + postfix )
    applyPostfix( process, 'patMuons', postfix ).isolationValues.pfPUChargedHadrons = cms.InputTag( 'muPFIsoValuePU03' + postfix )
    applyPostfix( process, 'patMuons', postfix ).isolationValues.pfPhotons          = cms.InputTag( 'muPFIsoValueGamma03' + postfix )
    applyPostfix( process, 'patMuons', postfix ).isolationValues.pfChargedHadrons   = cms.InputTag( 'muPFIsoValueCharged03' + postfix )
  applyPostfix( process, 'pfElectronsFromVertex'    , postfix ).vertices = cms.InputTag( pfVertices )
  applyPostfix( process, 'pfElectronsFromVertex'    , postfix ).d0Cut    = pfD0Cut
  applyPostfix( process, 'pfElectronsFromVertex'    , postfix ).dzCut    = pfDzCut
  applyPostfix( process, 'pfSelectedElectrons'      , postfix ).cut = pfElectronSelectionCut
  applyPostfix( process, 'pfIsolatedElectrons'      , postfix ).isolationCut = pfElectronCombIsoCut
  if pfElectronIsoConeR03:
    applyPostfix( process, 'pfIsolatedElectrons', postfix ).isolationValueMapsCharged  = cms.VInputTag( cms.InputTag( 'elPFIsoValueCharged03' + postfix )
                                                                                                      )
    applyPostfix( process, 'pfIsolatedElectrons', postfix ).deltaBetaIsolationValueMap = cms.InputTag( 'elPFIsoValuePU03' + postfix )
    applyPostfix( process, 'pfIsolatedElectrons', postfix ).isolationValueMapsNeutral  = cms.VInputTag( cms.InputTag( 'elPFIsoValueNeutral03' + postfix )
                                                                                                      , cms.InputTag( 'elPFIsoValueGamma03' + postfix )
                                                                                                      )
    applyPostfix( process, 'pfElectrons', postfix ).isolationValueMapsCharged  = cms.VInputTag( cms.InputTag( 'elPFIsoValueCharged03' + postfix )
                                                                                              )
    applyPostfix( process, 'pfElectrons', postfix ).deltaBetaIsolationValueMap = cms.InputTag( 'elPFIsoValuePU03' + postfix )
    applyPostfix( process, 'pfElectrons', postfix ).isolationValueMapsNeutral  = cms.VInputTag( cms.InputTag( 'elPFIsoValueNeutral03' + postfix )
                                                                                              , cms.InputTag( 'elPFIsoValueGamma03' + postfix )
                                                                                              )
    applyPostfix( process, 'patElectrons', postfix ).isolationValues.pfNeutralHadrons   = cms.InputTag( 'elPFIsoValueNeutral03' + postfix )
    applyPostfix( process, 'patElectrons', postfix ).isolationValues.pfChargedAll       = cms.InputTag( 'elPFIsoValueChargedAll03' + postfix )
    applyPostfix( process, 'patElectrons', postfix ).isolationValues.pfPUChargedHadrons = cms.InputTag( 'elPFIsoValuePU03' + postfix )
    applyPostfix( process, 'patElectrons', postfix ).isolationValues.pfPhotons          = cms.InputTag( 'elPFIsoValueGamma03' + postfix )
    applyPostfix( process, 'patElectrons', postfix ).isolationValues.pfChargedHadrons   = cms.InputTag( 'elPFIsoValueCharged03' + postfix )
  applyPostfix( process, 'patElectrons', postfix ).pvSrc = cms.InputTag( pfVertices )
  applyPostfix( process, 'patMuons'    , postfix ).pvSrc = cms.InputTag( pfVertices )

from TopQuarkAnalysis.Configuration.patRefSel_refMuJets_cfi import *

# remove MC matching, object cleaning, objects etc.
jecLevelsCalo = copy.copy( jecLevels )
if runStandardPAT:
  if not runOnMC:
    runOnData( process )
  # subsequent jet area calculations needed for L1FastJet on RECO jets
  if useCaloJets and useL1FastJet:
    if useRelVals:
      process.ak5CaloJets = ak5CaloJets.clone( doAreaFastjet = True )
      process.ak5JetID    = ak5JetID.clone()
      process.ak5CaloJetSequence = cms.Sequence(
        process.ak5CaloJets
      * process.ak5JetID
      )
      from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection
      switchJetCollection( process
                         , cms.InputTag( jetAlgo.lower() + 'CaloJets' )
                         , doJTA            = True
                         , doBTagging       = True
                         , jetCorrLabel     = ( jecSet, jecLevels )
                         , doType1MET       = False
                         , genJetCollection = cms.InputTag( jetAlgo.lower() + 'GenJets' )
                         , doJetID          = True
                         )
    else:
      print 'WARNING patRefSel_muJets_test_cfg.py:'
      print '        L1FastJet JECs are not available for AK5Calo jets in this data due to missing jet area computation;'
      print '        switching to   L1Offset   !!!'
      jecLevelsCalo.insert( 0, 'L1Offset' )
      jecLevelsCalo.remove( 'L1FastJet' )
      process.patJetCorrFactors.levels = jecLevelsCalo
      #process.patJetCorrFactors.useRho = False # FIXME: does not apply
  if usePFJets:
    if useL1FastJet:
      process.ak5PFJets = ak5PFJets.clone( doAreaFastjet = True )
    from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
    from PhysicsTools.PatAlgos.tools.metTools import addPfMET
    addJetCollection( process
                    , cms.InputTag( jetAlgo.lower() + pfSuffix + 'Jets' )
                    , jetAlgo
                    , pfSuffix
                    , doJTA            = True
                    , doBTagging       = True
                    , jetCorrLabel     = ( jecSetAddPF, jecLevels )
                    , doType1MET       = False
                    , doL1Cleaning     = False
                    , doL1Counters     = True
                    , genJetCollection = cms.InputTag( jetAlgo.lower() + 'GenJets' )
                    , doJetID          = True
                    )
    addPfMET( process
            , jetAlgo + pfSuffix
            )
  removeSpecificPATObjects( process
                          , names = [ 'Photons', 'Taus' ]
                          ) # includes 'removeCleaning'
if runPF2PAT:
  if not runOnMC:
    runOnData( process
             , names = [ 'PFAll' ]
             , postfix = postfix
             )
  removeSpecificPATObjects( process
                          , names = [ 'Photons', 'Taus' ]
                          , postfix = postfix
                          ) # includes 'removeCleaning'

# JetCorrFactorsProducer configuration has to be fixed in standard work flow after a call to 'runOnData()':
if runStandardPAT:
  process.patJetCorrFactors.payload = jecSet
  process.patJetCorrFactors.levels  = jecLevelsCalo

# additional event content has to be (re-)added _after_ the call to 'removeCleaning()':
process.out.outputCommands += [ 'keep edmTriggerResults_*_*_*'
                              , 'keep *_hltTriggerSummaryAOD_*_*'
                              # vertices and beam spot
                              , 'keep *_offlineBeamSpot_*_*'
                              , 'keep *_offlinePrimaryVertices*_*_*'
                              , 'keep *_goodOfflinePrimaryVertices*_*_*'
                              ]
if runOnMC:
  process.out.outputCommands += [ 'keep GenEventInfoProduct_*_*_*'
                                , 'keep recoGenParticles_*_*_*'
                                , 'keep *_addPileupInfo_*_*'
                                ]


###
### Additional configuration
###

goodPatJetsAddPFLabel = 'goodPatJets' + jetAlgo + pfSuffix

if runStandardPAT:

  ### Muons

  process.intermediatePatMuons = intermediatePatMuons.clone()
  process.loosePatMuons        = loosePatMuons.clone()
  process.step1a               = step1a.clone()
  process.tightPatMuons        = tightPatMuons.clone()
  process.step1b               = step1b.clone()
  process.step2                = step2.clone( src = cms.InputTag( 'selectedPatMuons' ) )

  if usePFJets:
    loosePatMuonsAddPF = loosePatMuons.clone()
    loosePatMuonsAddPF.checkOverlaps.jets.src = cms.InputTag( goodPatJetsAddPFLabel )
    setattr( process, 'loosePatMuons' + jetAlgo + pfSuffix, loosePatMuonsAddPF )
    step1aAddPF = step1a.clone( src = cms.InputTag( 'loosePatMuons' + jetAlgo + pfSuffix ) )
    setattr( process, 'step1a' + jetAlgo + pfSuffix, step1aAddPF )
    tightPatMuonsAddPF = tightPatMuons.clone( src = cms.InputTag( 'loosePatMuons' + jetAlgo + pfSuffix ) )
    setattr( process, 'tightPatMuons' + jetAlgo + pfSuffix, tightPatMuonsAddPF )
    step1bAddPF = step1b.clone( src = cms.InputTag( 'tightPatMuons' + jetAlgo + pfSuffix ) )
    setattr( process, 'step1b' + jetAlgo + pfSuffix, step1bAddPF )

  ### Jets

  process.kt6PFJets = kt6PFJets.clone( src          = cms.InputTag( 'particleFlow' )
                                     , doRhoFastjet = True
                                     )
  process.patDefaultSequence.replace( process.patJetCorrFactors
                                    , process.kt6PFJets * process.patJetCorrFactors
                                    )
  process.out.outputCommands.append( 'keep double_kt6PFJets_*_' + process.name_() )
  if useL1FastJet:
    process.patJetCorrFactors.useRho = True
    if usePFJets:
      getattr( process, 'patJetCorrFactors' + jetAlgo + pfSuffix ).useRho = True

  process.goodPatJets = goodPatJets.clone()
  process.step4a      = step4a.clone()
  process.step4b      = step4b.clone()
  process.step4c      = step4c.clone()
  process.step5       = step5.clone()

  if usePFJets:
    goodPatJetsAddPF = goodPatJets.clone( src = cms.InputTag( 'selectedPatJets' + jetAlgo + pfSuffix ) )
    setattr( process, goodPatJetsAddPFLabel, goodPatJetsAddPF )
    step4aAddPF = step4a.clone( src = cms.InputTag( goodPatJetsAddPFLabel ) )
    setattr( process, 'step4a' + jetAlgo + pfSuffix, step4aAddPF )
    step4bAddPF = step4b.clone( src = cms.InputTag( goodPatJetsAddPFLabel ) )
    setattr( process, 'step4b' + jetAlgo + pfSuffix, step4bAddPF )
    step4cAddPF = step4c.clone( src = cms.InputTag( goodPatJetsAddPFLabel ) )
    setattr( process, 'step4c' + jetAlgo + pfSuffix, step4cAddPF )
    step5AddPF = step5.clone( src = cms.InputTag( goodPatJetsAddPFLabel ) )
    setattr( process, 'step5' + jetAlgo + pfSuffix, step5AddPF )

  ### Electrons

  process.step3 = step3.clone( src = cms.InputTag( 'selectedPatElectrons' ) )

if runPF2PAT:

  ### Muons

  intermediatePatMuonsPF = intermediatePatMuons.clone( src = cms.InputTag( 'selectedPatMuons' + postfix ) )
  setattr( process, 'intermediatePatMuons' + postfix, intermediatePatMuonsPF )

  loosePatMuonsPF = loosePatMuons.clone( src = cms.InputTag( 'intermediatePatMuons' + postfix ) )
  setattr( process, 'loosePatMuons' + postfix, loosePatMuonsPF )
  getattr( process, 'loosePatMuons' + postfix ).checkOverlaps.jets.src = cms.InputTag( 'goodPatJets' + postfix )

  step1aPF = step1a.clone( src = cms.InputTag( 'loosePatMuons' + postfix ) )
  setattr( process, 'step1a' + postfix, step1aPF )

  tightPatMuonsPF = tightPatMuons.clone( src = cms.InputTag( 'loosePatMuons' + postfix ) )
  setattr( process, 'tightPatMuons' + postfix, tightPatMuonsPF )

  step1bPF = step1b.clone( src = cms.InputTag( 'tightPatMuons' + postfix ) )
  setattr( process, 'step1b' + postfix, step1bPF )

  step2PF = step2.clone( src = cms.InputTag( 'selectedPatMuons' + postfix ) )
  setattr( process, 'step2' + postfix, step2PF )

  ### Jets

  applyPostfix( process, 'patJetCorrFactors', postfix ).primaryVertices = cms.InputTag( pfVertices )
  setattr( process, 'kt6PFJets' + postfix, kt6PFJets )
  getattr( process, 'patPF2PATSequence' + postfix).replace( getattr( process, 'patJetCorrFactors' + postfix )
                                                          , getattr( process, 'kt6PFJets' + postfix ) * getattr( process, 'patJetCorrFactors' + postfix )
                                                          )
  if useL1FastJet:
    applyPostfix( process, 'patJetCorrFactors', postfix ).rho = cms.InputTag( 'kt6PFJets' + postfix, 'rho' )
  process.out.outputCommands.append( 'keep double_kt6PFJets' + postfix + '_*_' + process.name_() )

  goodPatJetsPF = goodPatJets.clone( src = cms.InputTag( 'selectedPatJets' + postfix ) )
  setattr( process, 'goodPatJets' + postfix, goodPatJetsPF )
  getattr( process, 'goodPatJets' + postfix ).checkOverlaps.muons.src = cms.InputTag( 'intermediatePatMuons' + postfix )

  step4aPF = step4a.clone( src = cms.InputTag( 'goodPatJets' + postfix ) )
  setattr( process, 'step4a' + postfix, step4aPF )
  step4bPF = step4b.clone( src = cms.InputTag( 'goodPatJets' + postfix ) )
  setattr( process, 'step4b' + postfix, step4bPF )
  step4cPF = step4c.clone( src = cms.InputTag( 'goodPatJets' + postfix ) )
  setattr( process, 'step4c' + postfix, step4cPF )
  step5PF = step5.clone( src = cms.InputTag( 'goodPatJets' + postfix ) )
  setattr( process, 'step5'  + postfix, step5PF  )

  ### Electrons

  step3PF = step3.clone( src = cms.InputTag( 'selectedPatElectrons' + postfix ) )
  setattr( process, 'step3' + postfix, step3PF )

process.out.outputCommands.append( 'keep *_intermediatePatMuons*_*_*' )
process.out.outputCommands.append( 'keep *_loosePatMuons*_*_*' )
process.out.outputCommands.append( 'keep *_tightPatMuons*_*_*' )
process.out.outputCommands.append( 'keep *_goodPatJets*_*_*' )


###
### Selection configuration
###

if runStandardPAT:

  ### Muons

  process.patMuons.usePV      = muonsUsePV
  process.patMuons.embedTrack = muonEmbedTrack

  process.selectedPatMuons.cut = muonCut

  process.intermediatePatMuons.preselection = looseMuonCut

  process.loosePatMuons.checkOverlaps.jets.deltaR = muonJetsDR
  if usePFJets:
    getattr( process, 'loosePatMuons' + jetAlgo + pfSuffix ).checkOverlaps.jets.deltaR = muonJetsDR

  process.tightPatMuons.preselection = tightMuonCut
  if usePFJets:
    getattr( process, 'tightPatMuons' + jetAlgo + pfSuffix ).preselection = tightMuonCut

  ### Jets

  process.goodPatJets.preselection = jetCut
  if usePFJets:
    getattr( process, goodPatJetsAddPFLabel ).preselection               = jetCutPF
    getattr( process, goodPatJetsAddPFLabel ).checkOverlaps.muons.deltaR = jetMuonsDRPF

  ### Electrons

  process.patElectrons.electronIDSources = electronIDSources

  process.selectedPatElectrons.cut = electronCut

if runPF2PAT:

  applyPostfix( process, 'patMuons', postfix ).usePV      = muonsUsePV
  applyPostfix( process, 'patMuons', postfix ).embedTrack = muonEmbedTrack

  applyPostfix( process, 'selectedPatMuons', postfix ).cut = muonCutPF

  getattr( process, 'intermediatePatMuons' + postfix ).preselection = looseMuonCutPF

  getattr( process, 'loosePatMuons' + postfix ).preselection              = looseMuonCutPF
  getattr( process, 'loosePatMuons' + postfix ).checkOverlaps.jets.deltaR = muonJetsDR

  getattr( process, 'tightPatMuons' + postfix ).preselection = tightMuonCutPF

  ### Jets

  getattr( process, 'goodPatJets' + postfix ).preselection               = jetCutPF
  getattr( process, 'goodPatJets' + postfix ).checkOverlaps.muons.deltaR = jetMuonsDRPF

  ### Electrons

  applyPostfix( process, 'patElectrons', postfix ).electronIDSources = electronIDSources

  applyPostfix( process, 'selectedPatElectrons', postfix ).cut = electronCutPF


###
### Trigger matching
###

if addTriggerMatching:

  if runOnMC:
    triggerObjectSelection = triggerObjectSelectionMC
  else:
    triggerObjectSelection = triggerObjectSelectionData
  ### Trigger matching configuration
  from PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cfi import patTrigger
  from TopQuarkAnalysis.Configuration.patRefSel_triggerMatching_cfi import patMuonTriggerMatch
  from PhysicsTools.PatAlgos.tools.trigTools import *
  if runStandardPAT:
    triggerProducer = patTrigger.clone()
    setattr( process, 'patTrigger', triggerProducer )
    process.triggerMatch = patMuonTriggerMatch.clone( matchedCuts = triggerObjectSelection )
    switchOnTriggerMatchEmbedding( process
                                 , triggerMatchers = [ 'triggerMatch' ]
                                 )
    removeCleaningFromTriggerMatching( process )
    process.intermediatePatMuons.src = cms.InputTag( 'selectedPatMuonsTriggerMatch' )
  if runPF2PAT:
    triggerProducerPF = patTrigger.clone()
    setattr( process, 'patTrigger' + postfix, triggerProducerPF )
    triggerMatchPF = patMuonTriggerMatch.clone( matchedCuts = triggerObjectSelection )
    setattr( process, 'triggerMatch' + postfix, triggerMatchPF )
    switchOnTriggerMatchEmbedding( process
                                 , triggerProducer = 'patTrigger' + postfix
                                 , triggerMatchers = [ 'triggerMatch' + postfix ]
                                 , sequence        = 'patPF2PATSequence' + postfix
                                 , postfix         = postfix
                                 )
    removeCleaningFromTriggerMatching( process
                                     , sequence = 'patPF2PATSequence' + postfix
                                     )
    getattr( process, 'intermediatePatMuons' + postfix ).src = cms.InputTag( 'selectedPatMuons' + postfix + 'TriggerMatch' )


###
### Scheduling
###

# CiC electron ID

process.load( "RecoEgamma.ElectronIdentification.cutsInCategoriesElectronIdentificationV06_cfi" )
process.eidCiCSequence = cms.Sequence(
  process.eidVeryLooseMC
+ process.eidLooseMC
+ process.eidMediumMC
+ process.eidTightMC
+ process.eidSuperTightMC
+ process.eidHyperTight1MC
+ process.eidHyperTight2MC
+ process.eidHyperTight3MC
+ process.eidHyperTight4MC
)

# The additional sequence

if runStandardPAT:
  process.patAddOnSequence = cms.Sequence(
    process.intermediatePatMuons
  * process.goodPatJets
  * process.loosePatMuons
  * process.tightPatMuons
  )
if runPF2PAT:
  patAddOnSequence = cms.Sequence(
    getattr( process, 'intermediatePatMuons' + postfix )
  * getattr( process, 'goodPatJets' + postfix )
  * getattr( process, 'loosePatMuons' + postfix )
  * getattr( process, 'tightPatMuons' + postfix )
  )
  setattr( process, 'patAddOnSequence' + postfix, patAddOnSequence )

# The paths
if runStandardPAT:

  if useCaloJets:

    process.p = cms.Path()
    if useTrigger:
      process.p += process.step0a
    process.p += process.goodOfflinePrimaryVertices
    if useGoodVertex:
      process.p += process.step0b
    if not runOnMC:
      process.p += process.step0c
    process.p += process.eidCiCSequence
    if useL1FastJet and useRelVals:
      process.p += process.ak5CaloJetSequence
    process.p += process.patDefaultSequence
    if usePFJets:
      process.p.remove( getattr( process, 'patJetCorrFactors'                    + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'jetTracksAssociatorAtVertex'          + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'impactParameterTagInfos'              + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'secondaryVertexTagInfos'              + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'softMuonTagInfos'                     + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'jetBProbabilityBJetTags'              + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'jetProbabilityBJetTags'               + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'trackCountingHighPurBJetTags'         + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'trackCountingHighEffBJetTags'         + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'simpleSecondaryVertexHighEffBJetTags' + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'simpleSecondaryVertexHighPurBJetTags' + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'combinedSecondaryVertexBJetTags'      + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'combinedSecondaryVertexMVABJetTags'   + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'softMuonBJetTags'                     + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'softMuonByPtBJetTags'                 + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'softMuonByIP3dBJetTags'               + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'patJetCharge'                         + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'patJetPartonMatch'                    + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'patJetGenJetMatch'                    + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'patJetPartonAssociation'              + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'patJetFlavourAssociation'             + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'patJets'                              + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'patMETs'                              + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'selectedPatJets'                      + jetAlgo + pfSuffix ) )
      process.p.remove( getattr( process, 'countPatJets'                         + jetAlgo + pfSuffix ) )
    process.p += process.patAddOnSequence
    if useLooseMuon:
      process.p += process.step1a
    if useTightMuon:
      process.p += process.step1b
    if useMuonVeto:
      process.p += process.step2
    if useElectronVeto:
      process.p += process.step3
    if use1Jet:
      process.p += process.step4a
    if use2Jets:
      process.p += process.step4b
    if use3Jets:
      process.p += process.step4c
    if use4Jets:
      process.p += process.step5
    process.out.SelectEvents.SelectEvents.append( 'p' )

  if usePFJets:

    pAddPF = cms.Path()
    if useTrigger:
      pAddPF += process.step0a
    pAddPF += process.goodOfflinePrimaryVertices
    if useGoodVertex:
      pAddPF += process.step0b
    if not runOnMC:
      pAddPF += process.step0c
    pAddPF += process.eidCiCSequence
    if useL1FastJet:
      pAddPF += process.ak5PFJets
    pAddPF += process.patDefaultSequence
    pAddPF.remove( process.patJetCorrFactors )
    if useCaloJets and useL1FastJet and useRelVals:
      pAddPF.remove( process.jetTracksAssociatorAtVertex )
      pAddPF.remove( process.impactParameterTagInfosAOD )
      pAddPF.remove( process.secondaryVertexTagInfosAOD )
      pAddPF.remove( process.softMuonTagInfosAOD )
      pAddPF.remove( process.jetBProbabilityBJetTagsAOD )
      pAddPF.remove( process.jetProbabilityBJetTagsAOD )
      pAddPF.remove( process.trackCountingHighPurBJetTagsAOD )
      pAddPF.remove( process.trackCountingHighEffBJetTagsAOD )
      pAddPF.remove( process.simpleSecondaryVertexHighEffBJetTagsAOD )
      pAddPF.remove( process.simpleSecondaryVertexHighPurBJetTagsAOD )
      pAddPF.remove( process.combinedSecondaryVertexBJetTagsAOD )
      pAddPF.remove( process.combinedSecondaryVertexMVABJetTagsAOD )
      pAddPF.remove( process.softMuonBJetTagsAOD )
      pAddPF.remove( process.softMuonByPtBJetTagsAOD )
      pAddPF.remove( process.softMuonByIP3dBJetTagsAOD )
    pAddPF.remove( process.patJetCharge )
    pAddPF.remove( process.patJetPartonMatch )
    pAddPF.remove( process.patJetGenJetMatch )
    pAddPF.remove( process.patJetPartonAssociation )
    pAddPF.remove( process.patJetFlavourAssociation )
    pAddPF.remove( process.patJets )
    pAddPF.remove( process.patMETs )
    pAddPF.remove( process.selectedPatJets )
    pAddPF.remove( process.countPatJets )
    pAddPF += process.patAddOnSequence
    pAddPF.replace( process.loosePatMuons
                  , getattr( process, 'loosePatMuons' + jetAlgo + pfSuffix )
                  )
    pAddPF.replace( process.tightPatMuons
                  , getattr( process, 'tightPatMuons' + jetAlgo + pfSuffix )
                  )
    pAddPF.replace( process.goodPatJets
                  , getattr( process, 'goodPatJets' + jetAlgo + pfSuffix )
                  )
    if useLooseMuon:
      pAddPF += getattr( process, 'step1a' + jetAlgo + pfSuffix )
    if useTightMuon:
      pAddPF += getattr( process, 'step1b' + jetAlgo + pfSuffix )
    if useMuonVeto:
      pAddPF += process.step2
    if useElectronVeto:
      pAddPF += process.step3
    if use1Jet:
      pAddPF += getattr( process, 'step4a' + jetAlgo + pfSuffix )
    if use2Jets:
      pAddPF += getattr( process, 'step4b' + jetAlgo + pfSuffix )
    if use3Jets:
      pAddPF += getattr( process, 'step4c' + jetAlgo + pfSuffix )
    if use4Jets:
      pAddPF += getattr( process, 'step5' + jetAlgo + pfSuffix )
    setattr( process, 'p' + jetAlgo + pfSuffix, pAddPF )
    process.out.SelectEvents.SelectEvents.append( 'p' + jetAlgo + pfSuffix )

if runPF2PAT:

  pPF = cms.Path()
  if useTrigger:
    pPF += process.step0a
  pPF += process.goodOfflinePrimaryVertices
  if useGoodVertex:
    pPF += process.step0b
  if not runOnMC:
    pPF += process.step0c
  pPF += process.eidCiCSequence
  pPF += getattr( process, 'patPF2PATSequence' + postfix )
  pPF += getattr( process, 'patAddOnSequence' + postfix )
  if useLooseMuon:
    pPF += getattr( process, 'step1a' + postfix )
  if useTightMuon:
    pPF += getattr( process, 'step1b' + postfix )
  if useMuonVeto:
    pPF += getattr( process, 'step2' + postfix )
  if useElectronVeto:
    pPF += getattr( process, 'step3' + postfix )
  if use1Jet:
    pPF += getattr( process, 'step4a' + postfix )
  if use2Jets:
    pPF += getattr( process, 'step4b' + postfix )
  if use3Jets:
    pPF += getattr( process, 'step4c' + postfix )
  if use4Jets:
    pPF += getattr( process, 'step5' + postfix )
  setattr( process, 'p' + postfix, pPF )
  process.out.SelectEvents.SelectEvents.append( 'p' + postfix )
