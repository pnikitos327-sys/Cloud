from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from django.utils import timezone
from django.db.models import Q
from .models import Folder, File
from .forms import FileUploadForm, FolderForm

def index(request):
    query = request.GET.get('q', '')
    
    folders = Folder.objects.filter(parent=None)
    files = File.objects.filter(folder=None, deleted_at__isnull=True)
    trash_files = File.objects.filter(user=request.user, deleted_at__isnull=False).order_by('-deleted_at')
    
    if query:
        files = files.filter(name__icontains=query)
    
    if request.method == 'POST':
        if 'file_upload' in request.POST:
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.save(commit=False)
                file.user = request.user
                file.size = request.FILES['file'].size
                file.save()
                return redirect('index')
        elif 'folder_create' in request.POST:
            folder_form = FolderForm(request.POST)
            if folder_form.is_valid():
                folder = folder_form.save(commit=False)
                folder.user = request.user
                folder.save()
                return redirect('index')
    
    form = FileUploadForm()
    folder_form = FolderForm()
    
    return render(request, 'storage/index.html', {
        'folders': folders,
        'files': files,
        'trash_files': trash_files,
        'form': form,
        'folder_form': folder_form,
    })

def download_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    file.downloads += 1
    file.save()
    
    # Получаем имя файла с расширением
    filename = file.file.name.split('/')[-1]
    
    response = FileResponse(file.file, as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

def toggle_favorite(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    file.favorite = not file.favorite
    file.save()
    return redirect('index')

def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    file.deleted_at = timezone.now()
    file.save()
    return redirect('index')

def restore_file(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    file.deleted_at = None
    file.save()
    return redirect('index')

def delete_permanent(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    file.file.delete()
    file.delete()
    return redirect('index')