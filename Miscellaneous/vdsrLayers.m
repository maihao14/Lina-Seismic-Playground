function layers = vdsrLayers()
%vdsrLayers    Create VDSR (Very Deep Super-resolution) network layers
%
%   layers = vdsrLayers() returns layers of the VDSR network
%
%   Example
%   -------
%
%   imds = imageDatastore(pathToNaturalImageData);
%
%   ds = vdsrImagePatchDatastore(imds,...
%     'MiniBatchSize',64,...
%     'PatchSize', 41,...
%     'BatchesPerImage',1,...
%     'ScaleFactor',4);
%
%   layers = vdsrLayers();
%
%   opts = trainingOptions('sgdm');
%
%   net = trainNetwork(ds,layers,opts);

%   Copyright 2017 The MathWorks, Inc.

% Reference
% ---------
%
% Kim, Jiwon, Jung Kwon Lee, and Kyoung Mu Lee. "Accurate image
% super-resolution using very deep convolutional networks." In Proceedings
% of the IEEE Conference on Computer Vision and Pattern Recognition 2016,
% pp. 1646-1654.

networkDepth = 20;

layers = imageInputLayer([41 41 1],'Name','InputLayer','Normalization','none');
convLayer = convolution2dLayer(3,64,...
    'Padding', 1, ...
    'Name', 'Conv1');

% He initialization
convLayer.Weights = sqrt(2/(9*64))*randn(3,3,1,64);
convLayer.Bias = zeros(1,1,64);

% Regularization set through training options
relLayer = reluLayer('Name', 'ReLU1');
layers = [layers convLayer relLayer];

for layerNumber = 2:networkDepth-1
    convLayer = convolution2dLayer(3, 64,...
        'Padding', [1 1],...
        'Name', ['Conv' num2str(layerNumber)]);
    % He initialization
    convLayer.Weights = sqrt(2/(9*64))*randn(3,3,64,64);
    convLayer.Bias = zeros(1,1,64);
    
    relLayer = reluLayer('Name', ['ReLU' num2str(layerNumber)]);
    layers = [layers convLayer relLayer];
end

convLayer = convolution2dLayer(3,1,...
    'NumChannels',64,...
    'Padding', [1 1],...
    'Name', ['Conv' num2str(networkDepth)]);
convLayer.Weights = sqrt(2/(9*64))*randn(3,3,64,1);
convLayer.Bias = zeros(1,1);

layers = [layers convLayer];
layers = [layers regressionLayer('Name','FinalRegressionLayer')];

end
