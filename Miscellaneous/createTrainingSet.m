function [prestineDirName,upsampledDirName,residualDirName] = createTrainingSet(imds,imds1)

while hasdata(imds) 
    % Use only the luminance component for training
    [I,info] = read(imds);
    I = rgb2ycbcr(I);
    Y = I(:,:,1);
    I = im2double(Y);
    
    [upsampledImage,info] = read(imds1);
    upsampledImage = rgb2ycbcr(upsampledImage);
    Y = upsampledImage(:,:,1);
    upsampledImage = im2double(Y);
%     % Randomly apply one value from scaleFactor
%     if isvector(scaleFactors)
%         scaleFactor = scaleFactors(randi([1 numel(scaleFactors)],1));
%     else
%         scaleFactor = scaleFactors;
%     end
    
%     upsampledImage = imresize(imresize(I,1/scaleFactor,'bicubic'),[size(I,1) size(I,2)],'bicubic');
    
     residualImage = I-upsampledImage;
%     residualImage = upsampledImage;
    [filePath, fileName, ~] = fileparts(info.Filename);
    if ~isfolder([filePath filesep 'pristineImages'])
        mkdir([filePath filesep 'pristineImages']);
    end
    
    if ~isfolder([filePath filesep 'residualImages'])
        mkdir([filePath filesep 'residualImages']);
    end
    
    if ~isfolder([filePath filesep 'upsampledImages'])
        mkdir([filePath filesep 'upsampledImages']);
    end
    extn = '.mat'; 
    
    save([filePath filesep 'pristineImages' filesep fileName extn],'I');
    save([filePath filesep 'residualImages' filesep fileName extn],'residualImage');
    save([filePath filesep 'upsampledImages' filesep fileName extn],'upsampledImage');
    prestineDirName = [filePath filesep 'pristineImages'];
    upsampledDirName = [filePath filesep 'upsampledImages'];
    residualDirName = [filePath filesep 'residualImages'];
    
end

end