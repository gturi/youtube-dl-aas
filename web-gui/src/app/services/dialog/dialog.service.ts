import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ErrorDialogComponent } from 'src/app/dialogs/error-dialog/error-dialog.component';
import { OptionsDialogComponent } from 'src/app/dialogs/options-dialog/options-dialog.component';

@Injectable({
  providedIn: 'root'
})
export class DialogService {

  constructor(private dialog: MatDialog) { }

  openErrorDialog(error: Error) {
    this.dialog.open(ErrorDialogComponent, {
      data: error
    });
  }

  openOptionsDialog(ydlOpts: Map<string, string | number>) {
    const dialogRef = this.dialog.open(OptionsDialogComponent, {
      data: ydlOpts
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
}